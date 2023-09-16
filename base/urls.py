from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name='room'),
    path('about/', views.about, name="about"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout")
    
]