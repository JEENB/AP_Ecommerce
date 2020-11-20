from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db.models import Avg, Count

# Create your models here.

#modle for  product
class Product(models.Model):
    STATUS   = (
        ('True', 'True'),
        ('False', 'False'),
    )
    FILTERS = (
        ('Smart', 'Smart'),
        ('Computer', 'Computer'),
        ('Laptop', 'Laptop'),
        ('Accessories', 'Accessories'),
    )
    category        = models.CharField(max_length = 18, choices = FILTERS)
    title           = models.CharField(max_length = 120)
    description     = models.CharField(max_length = 255)
    keywords        = models.CharField(max_length = 255)
    status          = models.CharField(max_length = 18, choices = STATUS)
    image           = models.URLField(default='')
    slug            = models.SlugField(unique = True, null = False, max_length=15)
    price           = models.DecimalField(max_digits = 50, decimal_places = 2)
    quantity        = models.IntegerField(blank = True, null = True)
    detail          = models.TextField()


    #for creating slug
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})
    
    #displays image beside product in db for aesthitics :P
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="40"/>'.format(self.image))
        else:
            return " No Image Found"
    image_tag.short_description = 'Image'


    #django aggregation to count reviews and average reviews
    def countrev(self):
        countreview = Review.objects.filter(product= self).aggregate(count=Count('id'))
        counter = int(countreview["count"])
        return counter

    def averagerev(self):
        averagereview = Review.objects.filter(product= self).aggregate(average=Avg('rate'))
        if averagereview["average"] is None:
            avg = 0
            return avg
        else:
            avg = float(averagereview["average"])
            return avg

# model to store multiple images for the same product
class Images(models.Model):
    product             = models.ForeignKey(Product, on_delete = models.CASCADE)
    image               = models.URLField(default='') 
    image_Description   = models.CharField(max_length = 50)

    def __str__(self):
        return (self.product.title)


class Review(models.Model):
    user    = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    comment = models.CharField(max_length=1000)
    rate    = models.IntegerField(default=1,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.product.title)

    @property
    def prod(self):
        return (self.product.title)
        
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rate']