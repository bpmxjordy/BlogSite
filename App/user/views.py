from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import postForm
from .models import post

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
    print(request.user.id)
    return render(request, "index.html")

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        user = request.user
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("/index/", user)
    else:
        form = AuthenticationForm()
    
    return render(request, "login.html", {"form": form})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return render(request, "index.html")

def register2(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form.save()
        return render(request, "index.html", {"form": request.POST["username"]})
    else:
        form = UserCreationForm()
    return render(request, "register2.html", {"form": form})

def createPost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = postForm(request.POST)
            if form.is_valid():
                form.user = request.user.username
                print(form.user)
                form.save()
                print(form)
            redirect("/posts/")
        form = postForm()
        return render(request, "createPost.html", {"form": form})
    else:
        redirect("/index/")

def posts(request):
    if request.user.is_authenticated:
        return render(request, "posts.html", {"posts":post.objects.all().values()})
    return redirect("/login/")
    