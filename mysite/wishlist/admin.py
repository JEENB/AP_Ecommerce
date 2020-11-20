from django.contrib import admin
from .models import WishlistCart
# Register your models here.


class AdminWishlistCart(admin.ModelAdmin):
    list_display = ['prod', 'user', 'created','price', 'updated' ]
    list_filter  = ['user', 'created'] 



admin.site.register(WishlistCart, AdminWishlistCart)