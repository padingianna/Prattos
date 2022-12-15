from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
"""from .forms import *"""
from datetime import *
from django.views.generic.edit import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



def index(request):
    return render(  request, 'home/index.html')

def nosotros(request):
    return render(  request, 'home/nosotros.html')

def contacto(request):
    return render(  request, 'home/contacto.html')



