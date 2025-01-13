from django.shortcuts import render
from django.views.generic import ListView
from .models import Chef, Recipe

class ChefView(ListView):
    model = Chef
    template_name = 'chef/main.html'
    context_object_name = 'chefs'