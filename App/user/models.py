from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    
    title = models.CharField(max_length= 50)
    description = models.CharField(max_length=1000)
    image = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    authorName = models.CharField(max_length=1000)