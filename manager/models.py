from django.db import models

# Create your models here.


class Table(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="items", default=None)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
