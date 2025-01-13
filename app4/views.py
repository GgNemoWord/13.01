from django.shortcuts import render
from .models import *
# Create your views here.
def main(request):
    school = School.objects.all()
    director = Director.objects.all()
    return render(request, 'school/index.html', {'schools': school, 'directors': director})
