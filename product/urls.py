from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path('',views.home,name='home'),
    path('detail',views.detail,name = "detail"),
    path('login',views.login,name='login')

]