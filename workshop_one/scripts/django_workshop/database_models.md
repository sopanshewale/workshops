```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

```

Let us create Models in dravate/models.py


```
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):  
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):      
        return self.title
```

Creating and Migrating Database

```

$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  No migrations to apply.
  Your models have changes that are not yet reflected in a migration, and so won't be applied.
  Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
$ python manage.py makemigrations
Migrations for 'dravate':
  dravate/migrations/0001_initial.py
    - Create model Category
    - Create model Page
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, dravate, sessions
Running migrations:
  Applying dravate.0001_initial... OK
$ 

```
Create Superuser 

```

$ python manage.py createsuperuser
Username (leave blank to use 'root'): admin@dravate.com      
Email address: info@dravate.com
Password: 
Password (again): 
Superuser created successfully.
$ 

```

Registering Models with Admin Interface - update dravate/admin.py 


```
from django.contrib import admin
from dravate.models import Category, Page

admin.site.register(Category)
admin.site.register(Page)
```

Copy script - populate_dravate.py

```
$ python populate_dravate.py 
Starting Dravate population script...
- Python - Official Python Tutorial
- Python - How to Think like a Computer Scientist
- Python - Learn Python in 10 Minutes
- Django - Official Django Tutorial
- Django - Django Rocks
- Django - Five Reasons why you should learn Django
- Other Frameworks - Bottle
- Other Frameworks - Flask
$ 

```

