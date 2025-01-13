from django.db import models

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=20)
    library = models.ForeignKey(Library, on_delete=models.PROTECT)
    def __str__(self):
        return self.name
