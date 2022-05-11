from django.http.response import HttpResponse
from django.urls import path
from . import views



urlpatterns = [
    path("home", views.u_home, name="user-home"),
    path("login", views.u_login, name="user-login"),
    path("logout", views.u_logout, name="user-logout"),
    path("register", views.u_register, name="user-register"),
    path("join-creator", views.u_join_creator, name="user-join-creator"),
    
]