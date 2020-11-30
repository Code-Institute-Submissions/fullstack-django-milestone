from django.db import models
from django.contrib.auth.models import User
from products.models import Ebook
# Create your models here.

class ShoppingCart(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ebook)

    def __str__(self):
        return self.customer.username

class Order(models.Model):
    ref =  models.CharField(max_length=50)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ebook)
    amount_paid = models.DecimalField(max_digits=10,decimal_places=2)
    date_of_purchase = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.username
