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
    path("home/post/add", add_post, name="add_post"),           
    path("home/post/edit/<int:pk>", edit_post, name="edit_post"),           
    path("home/post/del/<int:pk>", delete_post, name="delete_post"),           
    path("home/post/show/<slug:slug>", post_page, name="post_page"),           

#-----------------------------------------------------
    path("dashboard/<str:username>/", dashboard, name="dashboard"),           



]