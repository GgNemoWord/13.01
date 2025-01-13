from django.urls import path
from . import views

urlpatterns = [
    path('main', views.DeviceView.as_view(), name='main'),
    path('delete/<int:pk>', views.DeviceDelete.as_view(), name='delete'),
]