from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from .views import *

urlpatterns = [
#-----------------------------------------------------
    path("home/",home_page, name="home"),
    path("",lambda request : redirect('home/')),            # home urls 
#-----------------------------------------------------
    # path("home/post/<slug:slug>", views., name="post_detail"),           # posts urls

#-----------------------------------------------------



]