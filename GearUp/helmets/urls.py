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
    path('profile',views.profile,name='profile'),
    path('table',views.table,name='table'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
   
   
]