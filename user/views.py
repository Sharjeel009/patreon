from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from creator.models import Tier

from user.models import UserDetails
from .forms import CreatorDetailsForm

# Create your views here.
def u_home(request):
    return render(request, 'user_home.html')

def u_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(username=email)
        except:
            print("Username does not exist")
        user = authenticate(request, username=email, password=password)
        

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            print("Invalid Password")

    return render(request, 'login.html')

def u_logout(request):
    logout(request)
    return redirect("home")


def u_register(request):
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        user = User.objects.create_user(
            first_name = firstname,
            last_name = lastname,
            email = email,
            username = email,
            password = password
        )
        return redirect('user-login')
        

    return render(request, 'register.html')

def u_join_creator(request):
    form = CreatorDetailsForm()

    if request.method == 'POST':
        form = CreatorDetailsForm(request.POST, request.FILES)
        if form.is_valid:
            u_details = UserDetails.objects.get(user = request.user)
            u_details.is_creator = True
            u_details.save(update_fields=["is_creator"]) 

            c_details = form.save(commit=False)
            c_details.user = request.user
            c_details.save()

            tier1title = request.POST['tier1title']
            tier1price = request.POST['tier1price']
            tier1desc = request.POST['tier1desc']
            Tier.objects.create(user=request.user, title=tier1title, price=tier1price, desc=tier1desc)

            tier2title = request.POST['tier2title']
            tier2price = request.POST['tier2price']
            tier2desc = request.POST['tier2desc']
            Tier.objects.create(user=request.user, title=tier2title, price=tier2price, desc=tier2desc)

            tier3title = request.POST['tier3title']
            tier3price = request.POST['tier3price']
            tier3desc = request.POST['tier3desc']
            Tier.objects.create(user=request.user, title=tier3title, price=tier3price, desc=tier3desc)

    context = {'form' : form}
    return render(request, 'join_creator.html', context)