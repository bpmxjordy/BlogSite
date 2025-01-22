from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            auth_login(request, form.save())
            return render(request, 'index.html')
    else:
        form = UserCreationForm().as_p
    return render(request, 'register.html', {"form": form})

def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("/index/")
    else:
        form = AuthenticationForm()
    
    return render(request, "login.html", {"form": form})

def register2(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form.save()
        return render(request, "index.html", {"form": request.POST["username"]})
    else:
        form = UserCreationForm()
    return render(request, "register2.html", {"form": form})