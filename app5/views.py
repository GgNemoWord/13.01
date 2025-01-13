from django.shortcuts import render
from .models import *
# Create your views here.
def main(request):
    records = Record.objects.all()
    sportsmans = Sportsman.objects.all()
    return render(request, 'sportsman/index.html', {'records': records, 'sportsmans': sportsmans})
