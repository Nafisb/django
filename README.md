# django-api
Building Rest APIs with django


### Requirements
- Anaconda
- Python

### How to run the code
1. Set your current directory where you can see the file environment.yml.
2. Run this command: "conda env create --file environment.yml".
3. Then, run: "conda activate django-env".
4. Finally, run "python manage.py runserver".
5. Run: "python manage.py makemigrations".
6. Run "python manage.py migrate".
7. Open the url in your browser to invoke the APIs.

### How to call the APIs
- "/api", to see the list of implemented APIs.
- "/api/user/register", to register a new user.
- "/api/user/login", to login as an already registered user. The endpoint returns the authentication Token. Example request: {"username":"user1","password":"pass1"}
- "/api/user/all", to see the list of users. Note that only authenticated users can see the list. Example request: curl -X GET http://127.0.0.1:8000/api/user/all/ -u user1:pass1
- /api/network/all", to see the list of networks.
- "api/network/create", to create a new network. Each network must have a "title", but "description" is optional. Example request: {"title": "new network", "description":"creating a new network."}
- "/api/network/update/<str:id>", to update an existing network. Example request: {"title": "new network", "description":"updating the network."}
- "/api/network/delete/<str:id>", to delete an existing network. After sending the request, you have to confirm that you want to delete the network.

### How to run the tests
- Stop the server.
- Run: "manage.py migrate --run-syncdb".
- Run: "python manage.py test".

### Possible issues
In case of any error regarding the models or tables, try to restart the DB, by:
1. Delete the existing database which is db.sqlite3, located in the main directory.
2. Remove __pycache__ subdirectories.
3. Clear migrations ./base/migrations directory, except for __init__.py file.
4. Run: "python manage.py makemigrations"
5. Run: "python manage.py migrate"
