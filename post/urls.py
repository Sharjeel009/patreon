from django.http.response import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path("new", views.p_new, name="new-post"),
    path("text", views.p_text, name="new-post-text"),
    path("image", views.p_image, name="new-post-image"),
    path("video", views.p_video, name="new-post-video"),
    path("audio", views.p_audio, name="new-post-audio"),
    path("link", views.p_link, name="new-post-link"),
    path("poll", views.p_poll, name="new-post-poll"),
]