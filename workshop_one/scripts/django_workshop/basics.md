
# Basic Verification 

```
$ source bin/activate
$ 

$ python --version
Python 3.4.3


$ python -c "import django; print(django.get_version())"
1.11.1

```

# Starting Django Project 

```

$ django-admin startproject django_workshop
$ 
$ tree
.
`-- django_workshop
    |-- django_workshop
    |   |-- __init__.py
    |   |-- settings.py
    |   |-- urls.py
    |   `-- wsgi.py
    `-- manage.py

2 directories, 5 files

```

* *__init__.py*  - That's blank Python Script. Says it's Python Package. So anything, every module is available for *import*
* *settings.py* - Store your  Django project’s settings;
* *urls.py* a Python script to store URL patterns for your project; and
* *wsgi.py* a Python script used to help run your development server and deploy your project to a production environment.

# Starting Your Web Application 

```
$ cd django_workshop/
$ python manage.py runserver 
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

June 23, 2017 - 13:38:20
Django version 1.11.1, using settings 'django_workshop.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

Notice that line:

```

You have 13 unapplied migration(s).

```

Go ahead and run following command: 

```
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK

```

The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app


Notice now: 
```
$ tree
.
|-- db.sqlite3
|-- django_workshop
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- __init__.cpython-34.pyc
|   |   |-- settings.cpython-34.pyc
|   |   |-- urls.cpython-34.pyc
|   |   `-- wsgi.cpython-34.pyc
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py
```
Notice additional files. 

```
sqlite> .schema
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(80) NOT NULL UNIQUE);
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"));
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "group_id" integer NOT NULL REFERENCES "auth_group" ("id"));
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"));
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id"), "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "action_time" datetime NOT NULL);
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id"), "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "username" varchar(150) NOT NULL UNIQUE);
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
sqlite> 

```

Now you can start application 

```
$ python manage.py runserver 
Performing system checks...

System check identified no issues (0 silenced).
June 23, 2017 - 13:43:47
Django version 1.11.1, using settings 'django_workshop.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.


```

# Django Application 

A Django project is a collection of configurations and applications that together make up a given web application or website.
A Django application exists to perform a particular task.

Let us create Application called - *dravate* 

```
$ python manage.py startapp dravate

```

Now - notice the files: 

```

$ tree
.
|-- db.sqlite3
|-- django_workshop
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- __init__.cpython-34.pyc
|   |   |-- settings.cpython-34.pyc
|   |   |-- urls.cpython-34.pyc
|   |   `-- wsgi.cpython-34.pyc
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
|-- dravate
|   |-- admin.py
|   |-- apps.py
|   |-- __init__.py
|   |-- migrations
|   |   `-- __init__.py
|   |-- models.py
|   |-- tests.py
|   `-- views.py
`-- manage.py

4 directories, 17 files


```

 __init__.py, serving the exact same purpose as discussed previously;
models.py, a place to store your application’s data models - where you specify the entities and relationships between data;
tests.py, where you can store a series of functions to test your application’s code; and
views.py, where you can store a series of functions that take a clients’s requests and return responses.
admin.py, where you can register your models so that you can benefit from some Django machinery which creates an admin interface for you (see #TODO(leifos):add link to admin chapter)


Time to tell your Django about your new application *dravate* 

```
# file: django_workshop/settings.py



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dravate',
]

```

Try Again ... if it gives error then something is wrong 

NOTE - I am starting on 9090 port 

```
$ python manage.py runserver 0:9090
Performing system checks...

System check identified no issues (0 silenced).
June 23, 2017 - 14:01:59
Django version 1.11.1, using settings 'django_workshop.settings'
Starting development server at http://0:9090/
Quit the server with CONTROL-C.
[23/Jun/2017 14:02:00] "GET / HTTP/1.1" 200 1716

```

# Create new *View* 

```
#file: dravate/views.py 

$ cat views.py 
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Dravate says hey there world!")


```


We first import the HttpResponse object from the django.http module.
Each view exists within the views.py file as a series of individual functions. In this instance, we only created one view - called index.
Each view takes in at least one argument - a HttpRequest object, which also lives in the django.http module. Convention dictates that this is named request, but you can rename this to whatever you want if you so desire.
Each view must return a HttpResponse object. A simple HttpResponse object takes a string parameter representing the content of the page we wish to send to the client requesting the view.



# Let us map the URL 

```
# file: dravate\urls.py 

$ cat urls.py 
from django.conf.urls import url
from dravate import views

urlpatterns = [url(r'^$', views.index, name='index'),]

```

Now try: 

```

 python manage.py runserver 0:9090


Performing system checks...

System check identified no issues (0 silenced).
June 23, 2017 - 14:15:21
Django version 1.11.1, using settings 'django_workshop.settings'
Starting development server at http://0:9090/
Quit the server with CONTROL-C.
[23/Jun/2017 14:15:23] "GET /dravate/ HTTP/1.1" 200 29

```

You can happily access 

```
http://localhost:9090/dravate/
```


# Task - 1
How about creating http://localhost:9090/dravate/about? 


