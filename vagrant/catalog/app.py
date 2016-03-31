from flask import Flask, render_template, g, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from catalog_setup import Base, Category, Item, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
from functools import wraps
from dict2xml import dict2xml as xmlify
from flask.ext.seasurf import SeaSurf

app = Flask(__name__)
csrf = SeaSurf(app)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog"

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create anti-forgery state token


@app.route('/login')
def show_login():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

# Connect to the Google API
@csrf.exempt
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check if the user is already logged in
    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    # Store user data in the session
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = get_user_ID(data["email"])
    if not user_id:
        user_id = create_user(login_session)
    login_session['user_id'] = user_id

    # Display confirmation message for successful login
    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<h1 class="redirect">Redirecting...</h1>'
    flash("you are now logged in as %s" % login_session['username'])
    return output

# User Helper Functions

# Create a new user


def create_user(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

# Get info about the user from the User table


def get_user_info(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user

# Get the user's email  for authorization checks during the session


def get_user_ID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

# DISCONNECT - Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials.access_token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] != '200':
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

# Create a login_required decorator function


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            return redirect(url_for('show_login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# Get a list of all categories in the database
@app.route('/')
@app.route('/categories/')
def categories_list():
    categories = session.query(Category)
    return render_template('categoryList.html', categories=categories)

# Show the category page for the selected category
# List all items that belong to that category
@app.route('/categories/<int:category_id>/')
def show_category(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id)
    if 'username' not in login_session:
        return render_template(
            'publicCategory.html',
            category=category,
            items=items)
    else:
        return render_template('category.html', category=category, items=items)

# edit a category if user is the author
@app.route('/categories/<int:category_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_category(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    if category.user_id == login_session['user_id']:
        if request.method == 'POST':
            if request.form['category-name']:
                category.name = request.form['category-name']
            session.add(category)
            session.commit()
            return redirect(url_for('show_category', category_id=category.id))
        else:
            return render_template('editCategory.html', category=category)
    else:
        return "<script>function myFunction() {alert('You are not authorized to " \
        "edit this category. You may only edit a category you have created.'); " \
        "window.history.back();}</script><body onload='myFunction()''>"

@app.route('/categories/<int:category_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_category(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if category.user_id == login_session['user_id']:
        if request.method == 'POST':
            session.delete(category)
            session.commit()
            return redirect(url_for('categories_list'))
        else:
            return render_template('deleteCategory.html', category=category)
    else:
        return "<script>function myFunction() {alert('You are not authorized to " \
        "delete this category. You may only delete a category you have created.'); " \
        "window.history.back();}</script><body onload='myFunction()''>"


@app.route('/categories/add', methods=['GET', 'POST'])
@login_required
def new_category():
    if request.method == 'POST':
        newCategory = Category(
            name=request.form['category-name'],
            user_id=login_session['user_id'])
        session.add(newCategory)
        flash('New Category %s Successfully Created!' % newCategory.name)
        session.commit()
        return redirect(url_for('categories_list'))
    else:
        return render_template('newCategory.html')


@app.route('/categories/<int:category_id>/<int:item_id>/')
def show_item(item_id, category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    if 'username' not in login_session:
        return render_template('publicItem.html', item=item, category=category)
    else:
        return render_template('item.html', item=item, category=category)


@app.route('/categories/<int:category_id>/<int:item_id>/edit',
    methods=['GET','POST'])
@login_required
def edit_item(item_id, category_id):
    item = session.query(Item).filter_by(id=item_id).one()
    category = session.query(Category).filter_by(id=category_id).one()
    if item.user_id == login_session['user_id']:
        if request.method == 'POST':
            if request.form['item-name']:
                item.name = request.form['item-name']
            if request.form['item-description']:
                item.description = request.form['item-description']
            if request.form['item-price']:
                item.price = request.form['item-price']
            if request.form['item-image']:
                item.image = request.form['item-image']
            session.add(item)
            session.commit()
            return redirect(
                url_for(
                    'show_item',
                    item_id=item.id,
                    category_id=item.category_id))
        else:
            return render_template(
                'editItem.html', item=item, category=category)
    else:
        return "<script>function myFunction() {alert('You are not authorized to " \
        "edit this item. Please create your own item in order to edit.'); " \
        "window.history.back();}</script><body onload='myFunction()''>"


@app.route(
    '/categories/<int:category_id>/<int:item_id>/delete',
    methods=[
        'GET',
        'POST'])
@login_required
def delete_item(category_id, item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    category = session.query(Category).filter_by(id=category_id).one()
    if item.user_id == login_session['user_id']:
        if request.method == 'POST':
            session.delete(item)
            session.commit()
            return redirect(
                url_for(
                    'show_category',
                    category_id=item.category_id))
        else:
            return render_template(
                'deleteItem.html',
                item=item,
                category=category)
    else:
        return "<script>function myFunction() {alert('You are not authorized to" \
        " delete this item. You may only delete an item you have created.');" \
        "window.history.back();}</script><body onload='myFunction()''>"


@app.route('/categories/<int:category_id>/add', methods=['GET', 'POST'])
@login_required
def new_item(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        newItem = Item(
            name=request.form['item-name'],
            description=request.form['item-description'],
            price=request.form['item-price'],
            image=request.form['item-image'],
            category_id=category_id,
            user_id=login_session['user_id'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('show_category', category_id=category.id))
    else:
        return render_template('newItem.html', category=category)


@app.route('/disconnect')
def disconnect():
    gdisconnect()
    del login_session['gplus_id']
    del login_session['access_token']
    del login_session['username']
    del login_session['email']
    del login_session['picture']
    del login_session['user_id']
    del login_session['provider']
    flash("You have successfully been logged out.")
    return redirect(url_for('categories_list'))

# JSON APIs to view Restaurant Information


@app.route('/categories/JSON')
def categories_list_JSON():
    categories = session.query(Category).all()
    return jsonify(categories=[c.serialize for c in categories])


@app.route('/categories/<int:category_id>/JSON')
def category_JSON(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(
        category_id=category_id).all()
    return jsonify(Items=[i.serialize for i in items])


@app.route('/categories/<int:category_id>/<int:item_id>/JSON')
def item_JSON(category_id, item_id):
    item = session.query(Item).filter_by(id=category_id).one()
    return jsonify(item=item.serialize)


@app.route('/JSON')
def all_items_JSON():
    items = session.query(Item).all()
    return jsonify(Items=[i.serialize for i in items])


@app.route('/categories/xml')
def categories_list_xml():
    categories = session.query(Category).all()
    output = ''
    for c in categories:
        xml = xmlify(c.serialize, wrap="all", indent="  ", newlines=True)
        output += xml
        output += '</br>'
    return output


@app.route('/categories/<int:category_id>/xml')
def category_xml(category_id):
    items = session.query(Item).filter_by(
        category_id=category_id).all()
    output = ''
    for i in items:
        xml = xmlify(i.serialize, wrap="all", indent="  ", newlines=True)
        output += xml
        output += '</br>'
    return output

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
