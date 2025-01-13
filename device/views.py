from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Device
from django.views.generic import ListView, DeleteView


class DeviceView(ListView):
    model = Device
    template_name = 'device/main.html'
    context_object_name = 'devices'


class DeviceDelete(DeleteView):
    model = Device
    template_name = 'device/confirm.html'
    success_url = reverse_lazy('main')