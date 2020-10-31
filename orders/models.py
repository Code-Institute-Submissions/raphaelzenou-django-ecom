from django.db import models

# Create your models here.
from products.models import Product
from storemain.models import User

import uuid
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, 
    editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, 
    blank=True, null=True)
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=False
        )
    first_name = models.CharField(max_length=100, unique=False)
    last_name = models.CharField(max_length=100, unique=False)
    in_cart = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=100, unique=False)
    postcode = models.CharField(max_length=100, unique=False)
    city = models.CharField(max_length=100, unique=False)
    county_state = models.CharField(max_length=100, unique=False, blank=True)
    country = models.CharField(max_length=100, unique=False)
    delivery_cost = models.DecimalField(max_digits=7, decimal_places=2, 
    null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shipping_required = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    class Meta:
        db_table = "orders"
        verbose_name_plural = "Orders"

    def __str__(self):
        return str(self.id)
    
    @property
    def get_email(self):
        user = self.user
        if user:
            return user.email

    @property
    def get_first_name(self):
        user = self.user
        if user:
            return user.first_name

    @property
    def get_last_name(self):
        user = self.user
        if user:
            return user.last_name

    @property
    def get_quantity(self):
        orderproducts = self.orderproduct_set.all()
        quantity = sum([orderproduct.quantity for orderproduct \
            in orderproducts])
        return quantity

    @property
    def get_value(self):
        orderproducts = self.orderproduct_set.all()
        value = sum([orderproduct.get_value for orderproduct \
            in orderproducts])
        return value

class OrderProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, 
    editable=False)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, 
    blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, 
    blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "order_products"
        verbose_name_plural = "Order Products"

    def __str__(self):
        return str(self.quantity) + ' ' + self.product.title + ' id: ' \
            + str(self.order.id)
    
    @property
    def get_value(self):
        value = self.product.price_in_base_currency * self.quantity
        return value