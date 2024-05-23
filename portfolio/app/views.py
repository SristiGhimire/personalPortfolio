from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from django.conf import settings 
from django.contrib.auth.models import User

def index(request):
    return render(request, 'app/index.html')