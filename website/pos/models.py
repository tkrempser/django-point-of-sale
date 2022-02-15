from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField()
    commission = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at} - {self.customer.email}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    commission = models.FloatField(default=0.0)

    class Meta:
        unique_together = ('order', 'product')

    def __str__(self):
        return f"{self.order.created_at} - {self.order.customer.email} - {self.product.name} ({self.quantity})"
