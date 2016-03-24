from flask import Flask, render_template, request, redirect, url_for
from flask_oauthlib.client import OAuth
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from catalog_setup import Base, Category, Item

app = Flask(__name__)

oauth = OAuth()

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/categories/')
def categories_list():
    categories = session.query(Category)
    return render_template('categoryList.html', categories = categories)

@app.route('/categories/<int:category_id>/')
def show_category(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    items = session.query(Item).filter_by(category_id = category_id)
    return render_template('category.html', category = category, items = items)

@app.route('/categories/<int:category_id>/edit', methods=['GET', 'POST'])
def edit_category(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    if request.method == 'POST':
        if request.form['category-name']:
            category.name = request.form['category-name']
        session.add(category)
        session.commit()
        return redirect(url_for('show_category', category_id=category.id))
    else:
        return render_template('editCategory.html', category=category)

@app.route('/categories/<int:category_id>/delete', methods=['GET', 'POST'])
def delete_category(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    if request.method == 'POST':
        session.delete(category)
        session.commit()
        return redirect(url_for('categories_list'))
    else:
        return render_template('deleteCategory.html', category=category)

@app.route('/categories/<int:category_id>/<int:item_id>/')
def show_item(item_id, category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    item = session.query(Item).filter_by(id = item_id).one()
    return render_template('item.html', item=item, category=category)

@app.route('/categories/<int:category_id>/<int:item_id>/edit', methods=['GET', 'POST'])
def edit_item(item_id, category_id):
    item = session.query(Item).filter_by(id = item_id).one()
    category = session.query(Category).filter_by(id = category_id).one()
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
        return redirect(url_for('show_item', item_id=item.id, category_id=item.category_id))
    else:
        return render_template('editItem.html', item=item, category=category)

@app.route('/categories/<int:category_id>/<int:item_id>/delete', methods=['GET', 'POST'])
def delete_item(category_id, item_id):
    item = session.query(Item).filter_by(id = item_id).one()
    category = session.query(Category).filter_by(id = category_id).one()
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        return redirect(url_for('show_category', category_id=item.category_id))
    else:
        return render_template('deleteItem.html', item=item, category=category)

@app.route('/categories/<int:category_id>/add', methods=['GET', 'POST'])
def new_item(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    if request.method == 'POST':
        newItem = Item(name=request.form['item-name'], description=request.form['item-description'], price=request.form['item-price'], image=request.form['item-image'], category_id=category_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('show_category', category_id=category.id))
    else:
        return render_template('newItem.html', category=category)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)