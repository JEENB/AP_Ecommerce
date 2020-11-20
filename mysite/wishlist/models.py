from django.db import models

# Create your models here.
from django.db import models
from product.models import Product
from django.contrib.auth.models import User
from django.forms import ModelForm
from order.models import  Cart
# Create your models here.


class WishlistCart(models.Model):
    user        = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    product     = models.ForeignKey(Product, on_delete=models.SET_NULL, null= True)
    cart        = models.ForeignKey(Cart, on_delete=models.SET_NULL, null= True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    @property
    def prod(self):
        return (self.product.title)
 

    @property
    def price(self):
        return (self.product.price)



