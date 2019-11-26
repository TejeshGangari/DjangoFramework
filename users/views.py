from django.shortcuts import render, redirect
from .models import Customers

# Create your views here.

def register(request):
    if request.method == 'POST':
        print('In Request Method')
        custName = request.POST['custName']
        custFirstName = request.POST['custName']
        custLastName = request.POST['custName']
        custAddr = request.POST['custName']
        custPhone = request.POST['custName']
        custEmail = request.POST['custName']
        custPassword = request.POST['pass1']

        customer = Customers.objects.Create(custName=custName,custFirstName=custFirstName,custLastName=custLastName,custAddr=custAddr,custPhone=custPhone,custEmail=custEmail,custPassword=custPassword) 
        customer.save()
        return redirect('/')
    else:
        return render(request,'register.html')


def login(request):
    pass