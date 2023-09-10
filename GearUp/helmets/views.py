
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

def header(request):
    return(request,'header.html')
def home(request):
    return render(request,'home.html')
def fullface(request):
    return render(request,'fullface.html')
def login(request):
    if request.method=="POST":
        email=request.POST['email'] 
        password=request.POST['password']
        check_user=Customer.objects.filter(email=email,password=password).first()
        if check_user is not None:
            request.session['email']=email
            request.session['user_id']=check_user.id
            return redirect('home')
        else:
            return HttpResponse('-->Invalid credentials<--')
    return render(request,'log.html')
def logout1(request):
        logout(request)
        return HttpResponse('-->logged out Successfully Login Again to stay with us<--')
def checkout(request):
    return render(request,'checkout.html')
def register(request):
    if request.method=="POST":
        fullname=request.POST['fullname'] 
        username=request.POST['username'] 
        email=request.POST['email'] 
        Phone=request.POST['Phone']
        password=request.POST['password'] 
        confirm_password=request.POST['confirm_password'] 
        if password!=confirm_password:
            return HttpResponse("-->Registration not Done Your Password didn't match<--")
        else:
            check=Customer.objects.create(fullname=fullname,username=username,email=email,Phone=Phone,password=password,confirm_password=confirm_password)
            return HttpResponse('-->Registration Done Successfully<--')
    return render(request,'register.html')



