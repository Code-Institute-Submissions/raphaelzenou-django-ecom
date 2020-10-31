from django.contrib import admin

# Register your models here.
from .models import  User
from products.models import Product
from orders.models import Order, OrderProduct

# Register your models here.
admin.site.register(User)
admin.site.register(Product)

class OrderProductAdmin(admin.TabularInline):
    model = OrderProduct


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = (OrderProductAdmin,)

    readonly_fields = (
        'id', 
        'created_at',
        'updated_at',
        'get_email',
        'get_first_name',
        'get_last_name',
        'get_quantity',
        'get_value',
    )
    fields = (
        'id',
        'user',
        'get_email',
        'get_first_name',
        'get_last_name',
        'in_cart',
        'address',
        'postcode',
        'city',
        'county_state',
        'country',
        'shipping_required',
        'delivery_cost',
        'get_quantity',
        'get_value',
        'created_at',
        'updated_at',
    )

    list_display = (
        'id',
        'user'
    )
    # ordering = ('-created_at',)
    
admin.site.register(Order, OrderAdmin)