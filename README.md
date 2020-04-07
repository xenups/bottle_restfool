# ICE CREAM

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Requirements](https://img.shields.io/badge/Requirements-See%20Here-orange)](https://github.com/xenups/bottle_restfool/blob/master/requirements.txt)

<img src="https://raw.githubusercontent.com/xenups/bottle_restfool/master/ICECREAM/statics/images/ice.png" width="50" height="50">
ICE-CREAM framework for Bottle designed for simplify building restful api. It is structured such that any part of the core functionality can be customised to suit the needs of your project. every controller has access to each to reduce complex business logic.

**To run bottle builtin server with commands:**
    
    python manage.py runserver 
    python manage.py runserver 127.0.0.1:8000

**To bind icecream to gunicorn:**
    
    gunicorn --workers=2  'manage:wsgi_app()'

 
Copy and rename .env_example to .env and change the variable as project needs.
Or you can add the parameters manually into .env file
To generate an .env file these values are required:

| Variable Name                     | Description                    |
|-----------------------------------|--------------------------------|
| host                     | icecream host |
| port                     | icecream port |
| db_name                  | your database db_name|
| db_user                  | your database username|
| db_pass                  | your database password|
| db_host                  | your database host|
| db_port                  | your database port|
| project_secret            | needs for jwt authentication: experimental feature|
| jwt_ttl            | jwt time to live|
| sentry_dsn            | sentry address (logging tool), it can be|
| media_files            | static media folder|

already icecream is working with postgres

**to create new app:**

    python manage.py startapp app_name
    then register app in settings.py

#### **Migration Commands:**
**To initialize migration:** 

    alembic init alembic
    python manage.py makealembic
    

**To make migration:**

    alembic revision --autogenerate -m "Message"

**To migrate:**

    alembic upgrade head


 #### **File serving:**
**To serving files first  need to create a static folder in root of project:**

     Create a folder like :
    /statics/media/
**After that register the address in the .env:**

    media_files = /statics/media/
