from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Dravate Says Hello World!")
    context_d = {'boldmessage': "I am actually bold fond"}
    return render(request, 'dravate/index.html', context_d)

