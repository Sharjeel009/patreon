from django.http.response import HttpResponse
from django.urls import path
from . import views



urlpatterns = [
    path("", views.common_home, name="common-home")
]