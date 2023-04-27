from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user")
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    imageURL = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    costumer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name="customer")
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
    
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True, related_name="product")
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True, related_name="order")
    quantity = models.IntegerField(default=0, null=True, blank=True)
    dateItem = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    

class ShippingAdress(models.Model):
    costumer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name="customer_adress")
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name="order_adress")
    adress = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    zip = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adress


