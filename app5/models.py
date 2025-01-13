from django.db import models

# Create your models here.
class Record(models.Model):
    time = models.IntegerField()
    def __str__(self):
        return str(self.time)

class Sportsman(models.Model):
    name = models.CharField(max_length=20)
    record = models.OneToOneField(Record, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name + ' ' + str(self.record)
