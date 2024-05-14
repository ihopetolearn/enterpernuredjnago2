from django.db import models
from django.conf import settings
from .validators import vlidation_unit_measure,valid_unit_measurements


class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True,blank=True)
    descriptions = models.CharField(max_length=50, null=True,blank=True)
    direction = models.CharField(max_length=50, null=True,blank=True)
    timestamp = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True,blank=True)
    direction = models.CharField(max_length=50, null=True,blank=True)
    description = models.CharField(max_length=50, null=True,blank=True)
    quantity = models.CharField(max_length=50, null=True,blank=True)
    unit = models.CharField(max_length=50, validators= [vlidation_unit_measure], null=True)
    timestamp = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)






