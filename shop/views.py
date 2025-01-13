from django.shortcuts import render
from django.views.generic import ListView
from .models import Order, OrderItem

class OrderView(ListView):
    model = Order
    template_name = 'shop/main.html'
    context_object_name = 'orders'