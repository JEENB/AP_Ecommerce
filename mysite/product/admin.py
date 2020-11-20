from django.contrib import admin
from .models import Product
from .models import Images
from .models import Review
# Register your models here.





#adding extra image comes for Inline in models
class ImageFilter(admin.ModelAdmin):
    list_filter  = ['product.title']
class AdminImages(admin.TabularInline):
    model        = Images
    extra        = 3

class AdminProduct(admin.ModelAdmin):
    list_display        = ['title', 'price','category', 'status','image_tag' ]
    list_filter         = ['category', 'status']
    prepopulated_fields = {"slug": ("description",)}
    inlines             = [AdminImages]
    

class AdminReview(admin.ModelAdmin):
    list_display        = ['comment', 'rate', 'user', 'prod','created' ]
    list_filter         = ['product', 'user']


admin.site.register(Product, AdminProduct)
admin.site.register(Review, AdminReview)
admin.site.register(Images)

