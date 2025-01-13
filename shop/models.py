from django.db import models


class OrderItem(models.Model):
    number = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.number}'

class Order(models.Model):
    name = models.CharField(max_length=30)
    order = models.ForeignKey(OrderItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"Заказ {self.name} с номером: {self.order}"