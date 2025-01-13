from django.db import models


class Recipe(models.Model):
    ingre = models.CharField(max_length=100)

    def __str__(self):
        return self.ingre

class Chef(models.Model):
    name = models.CharField(max_length=30)
    recipe = models.ForeignKey(Recipe, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name}: {self.recipe}"
