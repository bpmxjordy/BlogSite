from user import views as user_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", user_view.register, name="register"),
    path("login/", user_view.login, name="login"),
    path("index/", user_view.index, name="index"),
    path("register2/", user_view.register2, name="register2"),
    path("logout/", user_view.logout, name="register2"),
    path("CreatePost/", user_view.createPost, name="CreatePost"),
    path("posts/", user_view.posts, name="posts")
]
