from django.shortcuts import render
from .models import Recipe, Ingredient
from django.views.generic import ListView

class RecipView(ListView):
    model = Recipe
    template_name = 'recipe/main.html'
    context_object_name = 'recipes'