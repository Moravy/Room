from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # from current folder import views
# from users app import views and name it users_view
from users import views as user_views
urlpatterns = [
    path('', views.home, name='chat-home'),
    path('about/', views.about, name='chat-about'),
    path('lobby/', views.lobby, name='chat-lobby'),
    path('general/', views.general, name='chat-general'),

    path('register/', user_views.register, name='user-register'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"),
         name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"),
         name='user-logout'),
    # path('/secretOnly/<room_name>/', views.room, name='chat-lobby'),
]
