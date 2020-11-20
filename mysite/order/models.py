from django.db import models
from product.models import Product
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.


class Cart(models.Model):
    user        = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    product     = models.ForeignKey(Product, on_delete=models.SET_NULL, null= True)
    quantity    = models.IntegerField()
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.product.title
        
    @property
    def prod(self):
        return (self.product.title)
 

    @property
    def price(self):
        return (self.product.price)

    @property
    def amount(self):
        return (self.product.price * self.quantity) 

     
class CartForm(ModelForm):
    class Meta:
        model   = Cart
        fields  = ['quantity']

class Order(models.Model):
    
    user        = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    first_name  = models.CharField(max_length= 250, null= True)
    last_name   = models.CharField(max_length= 250, null= True)
    email       = models.EmailField(max_length= 250, null= True)
    contact     = models.DecimalField(max_digits=10, decimal_places=0, null = True)
    pincode     = models.DecimalField(max_digits=6, decimal_places=0,null = True)
    address     = models.CharField(max_length=150,null = True)
    landmark    = models.CharField(max_length=50, null= True)
    city        = models.CharField(max_length=50,null = True)
    state       = models.CharField(max_length=50, null = True)
    country     = models.CharField(max_length=50,null = True, default = 'India')
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    STATUS = (
    ('Placed', 'Placed'),
    ('Accepted', 'Accepted'),
    ('Shipping', 'Shipping'),
    ('Complete', 'Complete'),
    ('Canceled', 'Canceled'),
                )
    status      = models.CharField(max_length = 20,choices= STATUS, default = 'Placed')
    ordercode   = models.CharField(max_length= 14)
    note        = models.CharField(max_length= 1000, null= True, blank= True)
    total       = models.FloatField(null = True)
    cname       = models.CharField(max_length=50, null= True, blank= False)
    ccnum       = models.CharField(max_length=16, null= True, blank= False)
    expmonth    = models.CharField(max_length=50, null= True, blank= False)  
    expyear     = models.CharField(max_length=50, null= True, blank= False)
    cvv         = models.CharField(max_length=3, null= True, blank= False)
    def __str__(self):
        return self.user.first_name


class OrderProduct(models.Model):
    user        = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    product     = models.ForeignKey(Product, on_delete=models.SET_NULL, null = True)
    order       = models.ForeignKey(Order, on_delete=models.CASCADE , null = True)
    price       = models.DecimalField(decimal_places= 2, max_digits= 1000000)
    quantity    = models.IntegerField()
    amount      = models.DecimalField(decimal_places= 2, max_digits= 1000000)
    shipping    = models.CharField(max_length= 500, null= True, blank= True)
    created     = models.DateTimeField(auto_now_add=True)

    STATUS      = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    status      = models.CharField(max_length= 20, choices= STATUS, default = 'New')

    def __str__(self):
        return self.product.title

    

    @property
    def prod(self):
        return (self.product.title)

class ShippingForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'contact','pincode','address', 'landmark', 'city', 'state', 'total', 'cname', 'ccnum', 'expmonth', 'expyear', 'cvv' ]