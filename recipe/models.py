from django.db import models

# Create your models here.

class Recipe(models.Model):
    dish = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)