# django-storages-poc
django storages as a backend to manage user files.

- storages contains files to boot up a local storage backend
- files is the django project
- you need to add files/config.py inside files which will contain secrets (simple key = "value" format. example entry in config.py. DEBUG = "True")

# how to check
- get a free tier postgresql instance from elephantsql for testing, update config.py with those secrets
- poetry install
- poetry shell (Activate virtual env) (to deactivate & exit virtualenv `exit`; to deactivate virtualenv `deactivate`)
- To test for ftp, uncomment ftp settings in STORAGES & comment out s3 settings in settings.py; to test for s3, do the vice versa.
- python files/manage.py runserver

# contents of files/config.py
SECRET_KEY = ""
DEBUG = True
ADMINPATH = "admin"

DB_NAME = ""
DB_USER = ""
DB_PASS = ""
DB_HOST = "" # i recommend elephantsql for testing. its free.

FTPUSER = ""
FTPPASS =""
FTPSERVER = ""
FTPPORT = 21

AWS_ACCESS_KEY_ID = "minioadmin"
AWS_SECRET_ACCESS_KEY = "minioadmin"
AWS_STORAGE_BUCKET_NAME = ""
AWS_S3_ENDPOINT_URL = "http://localhost:9000"