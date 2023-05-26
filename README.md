# django-storages-poc
django storages as a backend to manage user files.

- storages contains files to boot up a local storage backend
- files is the django project
- you need to add config.py inside files which will contain secrets (simple key = "value" format. example entry in config.py. DEBUG = "True")

# how to check
- get a free tier postgresql instance from elephantsql for testing, update config.py with those secrets
- poetry install
- poetry shell (Activate virtual env) (to deactivate & exit virtualenv `exit`; to deactivate virtualenv `deactivate`)
- python files/manage.py runserver

