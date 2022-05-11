from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from user.models import UserDetails
from .models import CreatorDetails, Tier

# Create your views here.
def c_home(request):
    return render(request, 'creator_home.html')

def c_edit_page(request):
    return HttpResponse("Creator Edit Page")

def c_view_page(request):
    return HttpResponse("Creator View Page")

def c_search_creator(request):
    queryString = request.GET.urlencode()
    queryString =  queryString[2:]
    creators = CreatorDetails.objects.filter(name__icontains=queryString)
    print(creators)
    context = {'creators' : creators}
    return render(request, 'search_creators.html', context)
    

def c_creator(request, slug):
    c_details = CreatorDetails.objects.get(slug = slug)
    tiers = Tier.objects.filter(user = c_details.user)
    context = {'creator' : c_details, 'tiers' : tiers}
    return render(request, 'view_creator.html', context)

def c_join_tier(request, tid):
    if request.method == 'POST':
        tier = Tier.objects.get(id=tid)
        tier.user_sub.add(UserDetails.objects.get(user = request.user))
        return redirect("home")
        
    if request.user.is_authenticated:
        return render(request, 'join_tier.html')
    else:
        return redirect("user-login")
