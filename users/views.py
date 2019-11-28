from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        custName = request.POST['custName']
        custFirstName = request.POST['custFirstName']
        custLastName = request.POST['custLastName']
        custAddr = request.POST['custAddr']
        custPhone = request.POST['custPhone']
        custEmail = request.POST['custEmail']
        custPassword = request.POST['pass1']
        confirmPassword = request.POST['pass2']
        if custPassword == confirmPassword:
            if User.objects.filter(username=custName).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=custEmail).exists():
                messages.error(request,'email taken')
                return redirect('register')
            else:
                customer = User.objects.create_user(username=custName,password=custPassword,email=custEmail,first_name=custFirstName,last_name=custLastName)
                customer.save()
        else:
            messages.error(request,'Password not matching')
            return redirect('register') 
        return redirect('/')  
    else:
        return render(request,'register.html')


def login(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')