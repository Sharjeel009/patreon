from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def p_new(request):
    return render(request, 'new_post.html')

def p_text(request):
    return render(request, 'new_post_text.html')

def p_image(request):
    return HttpResponse("Post New Image")

def p_video(request):
    return HttpResponse("Post New Video")

def p_audio(request):
    return HttpResponse("Post New Audio")

def p_link(request):
    return HttpResponse("Post New Audio")

def p_poll(request):
    return HttpResponse("Post New Audio")