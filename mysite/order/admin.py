from django.contrib import admin
from .models import Cart, Order, OrderProduct
# Register your models here.


class AdminCart(admin.ModelAdmin):
    list_display = [ 'prod','user', 'quantity', 'price', 'created']
    list_filter  = ['user', 'created'] 


class OrderProductline(admin.TabularInline):
    model           = OrderProduct
    extra           = 0
    can_delete      = False
    readonly_fields = ('user', 'prod', 'price', 'quantity', 'amount','product')

class AdminOrderProduct(admin.ModelAdmin):
    list_display    = ['user', 'prod', 'price','amount', 'quantity', 'status']
    readonly_fields = ('user', 'prod', 'price','amount', 'quantity',  'product', 'order')
    list_filter     = ['status', 'user']

class AdminOrder(admin.ModelAdmin):
    list_display    = ['first_name', 'email', 'contact','pincode','address', 'status', 'total']
    list_filter     = ['status', 'created', 'email']
    readonly_fields = ('first_name', 'last_name', 'email', 'contact','pincode','address', 'landmark', 'city', 'state', 'total', 'country','cname', 'ccnum','expmonth','expyear','cvv', 'ordercode')
    can_delete      = False
    inlines         = [OrderProductline]

admin.site.register(Cart, AdminCart)
admin.site.register(Order, AdminOrder)
admin.site.register(OrderProduct, AdminOrderProduct)