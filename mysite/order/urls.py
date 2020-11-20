from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/<int:id>', views.addtocart, name= 'addtocart'),
    path('remove/<int:id>', views.removecart, name= 'removecart'),
    path('billing/', views.orderproduct, name= 'orderproduct'),


]

