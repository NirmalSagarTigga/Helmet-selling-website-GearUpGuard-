from django.contrib import admin
from django.urls import  path
from .import views

urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('home',views.home,name='home'),
    path('logout',views.logout1,name='logout'),
    path('fullface',views.fullface,name='fullface'),
  
    
]