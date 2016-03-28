# Catalog Project
### To run this program:

1. Clone the repository to a machine that has VirtualBox and Vagrant already installed
2. In client_secrets.json, replace "YOUR_SECRET_KEY" with your client secret key
3. From the command line, navigate to the vagrant/tournament directory and initialize Vagrant
4. Login using vagrant ssh
5. Navigate back to /vagrant/catalog
6. Run app.py to initialize the catalog on your local port
7. Visit http://localhost:8000 to view the catalog

##### To add a category or item:
1. Login to the application using Google Sign In
2. Click on the '+ Add Category' icon on the category list page to add a category or the '+'  on a category landing page to add an item to a category.

##### To edit or delete a category or item:
1. Login to the application using Google Sign In
2. Click on the '-' icon to delete a category or item and the '?' to edit it.
* You may only edit or delete an item you have created.
