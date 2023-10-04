from django.contrib import admin
from django.urls import  path
from .import views

urlpatterns = [
    # path('',views.home,name='home'),
    path('admin_home/',views.dashboard,name='admin_home'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('forgot/',views.forgot_password,name='forgot'),
   
   
]
