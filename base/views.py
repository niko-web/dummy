# Create your views here.

from django.shortcuts import render
from .models import SiteUser
# from django.contrib.auth.models import User

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
