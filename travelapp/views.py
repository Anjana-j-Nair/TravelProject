from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team

# Create your views here.
def tr(request):
    P=Place.objects.all()
    T=Team.objects.all()#fetch cheyyan
    return render(request,"index.html",{'result':P,'res':T})
#result has all objects of model

# ORM is a programming technique that for converting data between relational db and object for the entire programming language
# ORM object relation map

# def addition(request):
#     x=int()