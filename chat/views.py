from django.shortcuts import render, redirect
from .form import roomForm
# Create your views here.


def home(request):
    # if request.method == 'POST':
    #     print("something")
    #     form = roomForm(request.POST)
    #     # room(request, room)
    # else:
    form = roomForm()
    return render(request, "chat/home.html", {"form": form})


def about(request):
    a = "ppppp"
    print(a)
    return render(request, "chat/about.html")


def register(request, userName, room_name):
    print(userName)
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
