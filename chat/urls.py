from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name='chat-home'),
    path('about/', views.about, name='chat-about'),
    path('lobby/', views.lobby, name='chat-lobby'),
    path('register/<str:username>', views.register, name='chat-register'),
    path('general/', views.general, name='chat-general'),
    # path('/secretOnly/<room_name>/', views.room, name='chat-lobby'),
]
