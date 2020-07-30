from django.shortcuts import render, redirect
from .form import userForm
from django.urls import reverse
# Create your views here.


def home(request):
    if request.method == 'POST':
        print("something")
        form = userForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data["userName"]

            return redirect('chat-register', username=userName)

        # room(request, room)
    else:
        form = userForm()
    return render(request, "chat/home.html", {"form": form})


def about(request):
    a = "ppppp"
    print(a)
    return render(request, "chat/about.html")


def register(request, username):
    print(username)
    return redirect('chat-lobby')


def room(request, room_name):
    print(room_name)
    return render(request, 'chat/room.html', {
        'room_name': room_name})


def lobby(request,):
    return render(request, 'chat/room.html', {'room_name': "lobby"})


def general(request):
    return render(request, 'chat/room.html', {'room_name': "general"})
# posts = [
#     {
#         'name': 'Jane doe',
#         'message': 'hello testing'
#     },
#     {
#         'name': 'Jonh doe',
#         'message': 'hello testing'
#     }
# ]
