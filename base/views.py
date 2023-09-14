# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SiteUser

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


    # context = {}
    return render(request, 'base/login_register.html')
