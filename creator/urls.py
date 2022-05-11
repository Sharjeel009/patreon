from django.http.response import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path("home", views.c_home, name="creator-home"),
    path("edit-page", views.c_edit_page, name="creator-edit-page"),
    path("view-page", views.c_view_page, name="creator-view-page"),
    path("s-creator", views.c_search_creator, name="search-creator"),
    path("details/<str:slug>", views.c_creator, name="view-creator"),
    path("jointier/<str:tid>", views.c_join_tier, name="join-tier"),
   
    
   
]