from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from .views import *


urlpatterns = [
#-----------------------------------------------------
    path("signup/", signupuser, name="signup"),
    path("login/", loginuser, name="login"),
    path("logout/", logoutuser, name="logout"),
    path("", lambda request : redirect("signup/")),
]