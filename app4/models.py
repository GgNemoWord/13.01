from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class School(models.Model):
    number = models.IntegerField()
    director = models.OneToOneField(Director, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.number)
