from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=30)
    instructions = models.ManyToManyField(Ingredient)

    def __str__(self):
        return f"{self.name}: {'/'.join([instructions.name for instructions in self.instructions.all()])}"
