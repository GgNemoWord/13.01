from django.shortcuts import render
from .models import *
# Create your views here.
def main(request):
    book = Book.objects.all()
    author = Author.objects.all()
    genre = Genre.objects.all()
    return render(request, 'book/index.html', {'books': book, 'authors': author, 'genres': genre})
