from django.shortcuts import render
from .models import *
# Create your views here.
def main(request):
    librarys = Library.objects.all()
    books = Book.objects.all()
    return render(request, 'library/index.html', {'librarys': librarys, 'books': books})
