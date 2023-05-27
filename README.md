# django-storages-poc
django storages as a backend to manage user files.

- storages contains files to boot up a local storage backend
- files is the django project
- you need to add files/config.py inside files which will contain secrets (simple key = "value" format. example entry in config.py. DEBUG = "True")

# how to check
- get a free tier postgresql instance from elephantsql for testing, update config.py with those secrets
- poetry install
- poetry shell (Activate virtual env) (to deactivate & exit virtualenv `exit`; to deactivate virtualenv `deactivate`)

# local ftp
- `make ftpup` brings up the ftp server
- `make ftpdown` brign down the ftp server

# local s3 minio storage
- `make s3up` brings up the s3 minio storage server
- `make s3down` brings down the s3 storage server
- go to AWS_S3_ENDPOINT_URL ("http://localhost:9000"), create a bucket

- test with s3
    - In settings.py comment out ftp settings in the STORAGES section. uncomment ftp settings if they are uncommented
    - `make runserver`
    - upload files in home page, files will be seen in your minio bucket

- test with ftp
    - In settings.py comment out s3 settings in the STORAGES section. uncomment s3 settings if they are uncommented
    - `make runserver`
    - upload files in home page, check files in storages/ftp/data section of this repo

# contents of files/config.py
SECRET_KEY = "" <br>
DEBUG = True <br>
ADMINPATH = "admin" <br>

DB_NAME = "" <br>
DB_USER = "" <br>
DB_PASS = "" <br>
DB_HOST = "" # i recommend elephantsql for testing. its free. <br>

FTPUSER = "" <br>
FTPPASS ="" <br>
FTPSERVER = "" <br>
FTPPORT = 21 <br>

AWS_ACCESS_KEY_ID = "minioadmin" <br>
AWS_SECRET_ACCESS_KEY = "minioadmin" <br>
AWS_STORAGE_BUCKET_NAME = "" <br>
AWS_S3_ENDPOINT_URL = "http://localhost:9000" <br>
