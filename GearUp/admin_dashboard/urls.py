from django.contrib import admin
from django.urls import  path
from .import views

urlpatterns = [
    path('',views.admin_home,name='admin_home'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('forgot/',views.forgot_password,name='forgot'),
    path('add_banner/',views.add_banner,name='add_banner'),
    path('add_product/',views.add_product,name='add_product'),
   
   
]
