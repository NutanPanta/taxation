# Taxation Core Backend

# Requirements

Please make sure they are installed before running the application

- Python 3.10

To install the dependencies, you can use the following command:

`pip3 install -r requirements.txt`

## Building Docker Image

`docker build -t <TAG NAME> .`

or

`docker compose up`

## Environment variables

```
DJANGO_SECRET_KEY='<RANDOMIZED KEY>'

ALLOWED_HOSTS='<ALLOWRD HOSTS>'

ALLOWED_ORIGINS='<ALLOWED ORIGINS>'

DJANGO_LOG_PATH="<PATH TO LOG FILE>"

DJANGO_LOG_LEVEL="<LOG LEVEL>"

DATABASE_NAME="<PG DATABASE NAME>"

DATABASE_USER="<PG DATABASE USER>"

DATABASE_PASSWORD="<PG DATABASE PASSWORD>"

DATABASE_HOST="<PG DATABASE HOST>"

DATABASE_PORT="<PG DATABASE PORT>"

CSRF_TRUSTED_ORIGINS="<CSRF TRUSTED ORIGINS>"

```

## API Documentation

All the api related documentation can be found inside **docs** folder within the repo.

**\*.postman_collection.json** is for importing collection to postman.
