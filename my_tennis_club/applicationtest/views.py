from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

def members(request):
    return HttpResponse("Hello world!")

def q(request):
    return render(request,'q.html',{'casenumber':'hello'})
    #template = loader.get_template('q.html')
    #return HttpResponse(template.render({'casenumber':'hello'}))



# Create your views here.



