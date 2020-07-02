## Hierarchical Data

The goal of this assignment was to learn about this type of database
and different ways of working with it. This was accomplished by
building a simple Django server that uses MPTT models from django-mptt
to create a Dropbox-esque web interface where you can create "folders"
and "files" in an arbitrary structure and then display that structure.
We didn't actually upload anything, just made model instances and
used them to represent real data. 

## How to test this project

1. Clone this repo to your local machine.

2. Poetry install.

3. Poetry shell.

4. Python manage.py createsuperuser.

5. Python manage.py makemigrations.

6. Python manage.py migrate.

7. Python manage.py runserver.

8. Enjoy!!!
