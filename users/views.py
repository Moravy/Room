from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


# if request method is a post check if its a valid
def register(request):
    if request.method == "POST":

        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            messages.success(request, f"done")
            return redirect('user-login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form})
