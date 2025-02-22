from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils import timezone

import json
from django.contrib.auth.models import User
# Create your models here.


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_des = models.TextField()
    recipe_image = models.ImageField(upload_to="recipes/")
    recipe_main = models.CharField(max_length=100, null=False, default='')    
    created_at = models.DateTimeField(auto_now_add=True)
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)  # Assuming Recipe model exists
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')  # Prevent duplicate favorites
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icon = models.ImageField(upload_to='category_icons/')
        
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

