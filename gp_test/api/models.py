from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Step(models.Model):
    step_text = models.TextField(max_length=255, null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="steps")

class Ingredient(models.Model):
    text = models.CharField(max_length=255, null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")



