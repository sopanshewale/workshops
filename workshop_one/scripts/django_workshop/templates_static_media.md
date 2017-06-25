```
$ mkdir -p templates/dravate

```

and create new file: 

```

$ more templates/dravate/index.html 
<!DOCTYPE html>
<html>

    <head>
        <title>Dravate</title>
    </head>

    <body>
        <h1>Dravate says...</h1>
        hello world! <strong>{{ boldmessage }}</strong><br />
        <a href="/dravate/about/">About</a><br />
    </body>

</html>


```

Modify dravate/views.py file 

```
$ more dravate/views.py 
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Dravate says hey there world!")
    context_dict = {'boldmessage': "I am bold font from the context"} 
    return render(request, 'dravate/index.html', context_dict)


$ 

```

How about static Files? 

```
mkdir static

```
possibly create images folder under static 

```
mkdir static/images

```
Modify django_workshop/settings.py 


```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

```

Add image in images folder: 

```
$ tree static/
static/
`-- images
    `-- django_demo_name.jpeg

1 directory, 1 file
$ 

```

Also modify templates/dravate/index.html to 

```
$ more templates/dravate/index.html 
<!DOCTYPE html>

{% load static %} <!-- New line -->

<html>

    <head>
        <title>Dravate</title>
    </head>

    <body>
        <h1>Dravate says...</h1>
        hello world! <strong>{{ boldmessage }}</strong><br />
        <a href="/dravate/about/">About</a><br />
        <img src="{% static "images/django_demo_name.jpeg" %}" alt="Picture of Django Django" /> <!-- New line -->
    </body>

</html>

$ 

```

Restart Application 

and access http://localhost:8888/dravate



