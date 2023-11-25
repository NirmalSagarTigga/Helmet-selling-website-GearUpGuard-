from django.contrib import admin
from django.urls import  path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('home',views.home,name='home'),
    path('logout',views.logout1,name='logout'),
    path('fullface',views.fullface,name='fullface'),
    path('offroad',views.offroad,name='offroad'),
    path('profile',views.profile,name='profile'),
    path('table',views.table,name='table'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('del_user/<id>',views.del_user,name='del_user'),
    path('product',views.product,name='product'),
	path('cart',views.cart,name='cart'),
   
   
]