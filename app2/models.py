from django.db import models

# Create your models here.
class Attendee(models.Model):
    name = models.CharField(max_length=20)
    registration_date = models.DateField()
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    attendee = models.ManyToManyField(Attendee)
    def __str__(self):
        return self.name
