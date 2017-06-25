Modify dravate/views.py 

```
from rango.models import Category
```

Modify templates/dravate/index.html

```
<!DOCTYPE html>

{% load static %} <!-- New line -->

<html>

    <head>
        <title>Dravate</title>
    </head>

    <body>
        <h1>Dravate says...</h1>

         {% if categories %}
            <ul>
                {% for category in categories %}
                <li>{{ category.name }}</li>
                {% endfor %}
            </ul>
        {% else %}
            <strong>There are no categories present.</strong>
        {% endif %}


        <a href="/dravate/about/">About</a><br />
        <img src="{% static "images/django_demo_name.jpeg" %}" alt="Picture of Django Django" /> <!-- New line -->
    </body>

</html>


```

Creating Detail Page 

We need support for
* /rango/category/1/ or /rango/category/2/, 
* /rango/category/Python/

Update dravate/models.py 

```
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Category, self).save(*args, **kwargs)



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

Now you need to run makemigrations

```
$ python manage.py makemigrations
You are trying to add a non-nullable field 'slug' to category without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> ''
Migrations for 'dravate':
  dravate/migrations/0003_category_slug.py
    - Add field slug to category

```
Now migrate

```
$ python manage.py migrate       
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, dravate, sessions
Running migrations:
  Applying dravate.0003_category_slug... OK
$ 

```

Let us modify dravate/admin.py 

```
from django.contrib import admin
from dravate.models import Category, Page

#admin.site.register(Category)
#admin.site.register(Page, PageAdmin)

class PageAdmin( admin.ModelAdmin):
   list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

```




