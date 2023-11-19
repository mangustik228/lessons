from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=120)
    desciption = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField()
    shipping_cost = models.FloatField()
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class ReceptionDesc(models.Model):
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, related_name="receiptions", null=True)
    length = models.IntegerField()
    height = models.IntegerField()
    title = models.CharField(max_length=250)
    price = models.FloatField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.title}[{self.color}]"
