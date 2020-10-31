from django.db import models

import uuid
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Product(models.Model): 
    # ID / primary key is created by django automatically 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=200, unique=True)
    price_in_base_currency = models.DecimalField(max_digits=7, decimal_places=2)
    sale_price_in_base_currency = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    on_sale = models.BooleanField(blank=False, null=True)
    
    CURRENCY_CHOICES = (
        ('GBP', '£'),
    )
    base_currency = models.CharField(max_length=3, default='GBP', choices=CURRENCY_CHOICES)
    options_csv = models.CharField(max_length=200, blank=True, null=True)

    CATEGORY_CHOICES = (
        ('LCH', 'Leads, Collars or Harnesses'),
        ('CLS', 'Clothes or Shoes'),
        ('FOT', 'Food and Treats'),
        ('ACC', 'Accessories'),
        ('GRO', 'Grooming'),
        ('CGK', 'Crates, Gates or Kennels'),
        ('BOO', 'Books - paperback'),
        ('DIG', 'Digital'),
        ('OTH', 'Other'),
    )
    category = models.CharField(max_length=3, blank=True, null=True, default='OTH',choices=CATEGORY_CHOICES)
    stock =  models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    class Meta:
        db_table = "products"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title