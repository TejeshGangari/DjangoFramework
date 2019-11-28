from django.shortcuts import render, redirect
from .models import Destination
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):

    dests = Destination.objects.all()
    return render(request,'index.html',{"desObjs":dests})

def destinations(request):
    if request.user.is_authenticated:
        return render(request,'destinations.html')
    else:
        return redirect('users/login')        
    