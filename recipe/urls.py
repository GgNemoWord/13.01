from django.urls import path
from . import views

urlpatterns = [
    path('main', views.RecipView.as_view(), name='main')
]