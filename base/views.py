# Create your views here.

from django.shortcuts import render
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
    context = {}
    return render(request, 'base/login_register.html', context)
