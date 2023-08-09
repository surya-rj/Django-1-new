from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import urls
# Create your views here.
def index(request):
    t=loader.get_template('index.html')
    return HttpResponse(t.render())
def index1(request):
    return HttpResponse("hi world team 1")
