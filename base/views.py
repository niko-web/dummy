# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SiteUser
from django.contrib.auth import authenticate, login, logout

def home(request):
    users = SiteUser.objects.all()

    context = {
        'users': users
    }
    
    return render(request, 'base/home.html', context)
  

def room(request):
    return render(request, 'base/room.html')

def about(request):
    return render(request, 'base/about.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = SiteUser.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist' )
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("room")
        else:
            messages.error(request, "username or password doesnt exist")


    
    return render(request, 'base/login_register.html')
