from django.shortcuts import render
# Create your views here.

rooms = [
    {
        'id':1, 
        'name': "Nikolay",

    },
    {
        'id':2, 
        'name': "georgi",

    },
    {
        'id':3, 
        'name': "Petar",

    },

]

def home(request):
    return render(request, 'home.html', {'rooms': rooms})

def room(request):
    return render(request, 'room.html')

def about(request):
    return render(request, 'about.html')
