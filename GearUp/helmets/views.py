
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

def home(request):
    return render(request,'home.html')

def fullface(request):
    return render(request,'fullface.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username'] 
        password=request.POST['password']
        check_user=Customer.objects.filter(username=username,password=password).first()
        if check_user is not None:
            request.session['username']=username
            request.session['user_id']=check_user.id
            return redirect('home')
        else:
            return HttpResponse('-->Invalid credentials<--')
    return render(request,'log.html')

def logout1(request):
        logout(request)
        return redirect('login')

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


def profile(request):
    if 'user_id' in request.session:
        profile_data=Customer.objects.get(id=request.session['user_id'])
        data={'profile':profile_data}
        return render(request,'profile.html',data)
    else:
        return redirect('login')
    
def table(request):
    user_list=Customer.objects.all()
    data={'user_list':user_list}
    return render(request,"table.html",data)

def edit_profile(request):
    if 'user_id' in request.session:
        if request.method == "POST":
            username = request.POST['username'] 
            # password = request.POST['password']
            email = request.POST['email']
            data = Customer.objects.get(id=request.session['user_id'])
            if username!="":
                data.username=username
            if email!="":
                data.email=email

            data.save()
            # messages.add_message(request, messages.success,"profile update sucessfully") 
            return redirect('profile')
        else:
            profile = Customer.objects.get(id=request.session['user_id'])
            data = {'profile':profile, 'title':'edit_profile'}
            return render(request, 'edit_profile.html', data)
    else:
        return redirect('login')

def del_user(request,id):
    check=Customer.objects.get(id=id)
    check.delete()
    messages.add_message(request,messages.SUCCESS,"user deleted")
    return redirect('table')

def product(request):
    product=Product.objects.all()
    data={'product':product}
    return render(request,'product.html',data) 


def cart(request):
    if request.method == "POST":
        if request.session['userid'] != '':
            pid=request.POST['pid']
            uid=request.session['userid']
            Cart.objects.create(product_id=pid,register_id=uid,qnty=1)
            return redirect('product') 
        else:
            cart=Cart.objects.all()
            data={'cart':cart}
            return render(request,'cart.html',data) 
    else:
        cart=Cart.objects.all()
        data={'cart':cart}
        return render(request,'cart.html',data)










