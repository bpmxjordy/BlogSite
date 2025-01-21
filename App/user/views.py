from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            return render(request, 'index.html', {"form": request.POST["username"]})
    else:
        form = UserCreationForm().as_p
    return render(request, 'register.html', {"form": form})

def index(request):
    return render(request, "index.html")

def register2(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form.save()
        return render(request, "index.html", {"form": request.POST["username"]})
    else:
        form = UserCreationForm()
    return render(request, "register2.html", {"form": form})