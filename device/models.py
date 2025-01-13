from django.db import models

class Number(models.Model):
    number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.number}"

class Device(models.Model):
    name = models.CharField(max_length=30)
    number = models.OneToOneField(Number, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} номер модели: {self.number}'
