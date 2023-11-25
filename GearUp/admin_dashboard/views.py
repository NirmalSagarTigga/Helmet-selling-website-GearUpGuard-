from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from helmets.models import *
from django.contrib import messages


# Create your views here.
def admin_home(request):
    return render(request,'index.html')

def admin_login(request):
    return render(request,'login.html')
    
def forgot_password(request):
    return render(request,'forgot.html')

def add_product(request):
    if request.method == "POST":
       image=request.FILES['image']
       pname=request.POST['pname']
       price=request.POST['price']
       pcolor=request.POST['pcolor']
       Product.objects.create(pname=pname,price=price,image=image,pcolor=pcolor)
       return redirect('add_product') 
    else:
        product=Product.objects.all()
        data={'product':product,'title':"Product | Admin"}
        return render(request,'add_product.html',data)
    
def add_banner(request):
    if request.method == "POST":
        bimage=request.FILES['bimage']
        Banner.objects.create(image=bimage)
        return redirect('add_banner')
    else:
        banner=Banner.objects.all()
        data={'banner':banner,'title':"Banner | Admin"}
        return render(request,'add_banner.html',data)
    
def del_banner(request,id):
    check=Banner.objects.get(id=id)
    check.delete()
    messages.add_message(request,messages.SUCCESS,"banner deleted")
    return redirect('add_banner')

def del_product(request,id):
    check=Product.objects.get(id=id)
    check.delete()
    messages.add_message(request,messages.SUCCESS,"Product deleted")
    return redirect('add_product')



