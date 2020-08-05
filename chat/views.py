from django.shortcuts import render, redirect
from .form import messagesForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Chat
from django.contrib.auth.models import User
# Create your views here.
# add userdatabase in model


def home(request):

    content = {
        "chats": Chat.objects.all()
    }

    return render(request, "chat/home.html", content)


def about(request):
    a = "ppppp"
    print(a)
    return render(request, "chat/about.html")


def register(request, username):
    print(username)
    return redirect('chat-lobby')


@login_required
def room(request, room_name):

    return render(request, 'chat/room.html', {
        'room_name': room_name})


@login_required
def lobby(request):
    if request.method == "POST":
        print("********WORKING*******")
        form = messagesForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data["messages"]
            print(message)
            newChat = newChat = Chat(message=message, user=request.user)
            newChat.save()
    else:
        form = messagesForm()
    return render(request, 'chat/room.html', {'form': form, "chats": Chat.objects.all(), 'room_name': "lobby", 'username': request.user.username})


@ login_required
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
