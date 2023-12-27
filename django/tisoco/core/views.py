from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hola mundo parte 2")

# Create your views here.
