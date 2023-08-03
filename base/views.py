from django.shortcuts import render
# Create your views here.

rooms = [
    {
        'id': 1,
        'name': 'Nikolay',
    },
    {
        'id': 2,
        'name': 'peter',
    },
    {
        'id': 3,
        'name': 'Ivan'
    },
]


def home(request):
    return render(request, 'base/home.html')

def room(request):
    context = {'rooms': rooms}
    return render(request, 'base/room.html', context)

def about(request):
    return render(request, 'base/about.html')
