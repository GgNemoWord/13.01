from django.db import models

class Profile(models.Model):
    title = models.CharField(max_length=30)

class User(models.Model):
    name = models.CharField(max_length=30)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
