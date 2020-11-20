from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home_page_view'),
    path('aboutus/', views.about_page_view, name='about_page_view'),
    path('contact/', views.contact_page_view, name='contact_page_view'),
    path('terms/', views.terms_page_view, name='terms_page_view'),
    path('products/computers/', views.computers_page_view, name='computer'),
    path('products/phones/', views.phones_page_view, name='phones'),
    path('products/accessories/', views.accessories_page_view, name='accessories'),
    path('products/laptops/', views.laptopss_page_view, name='lapt'),
    path('search/', views.search_page_view, name='search_page_view'),
    path('search_ajax/', views.search_ajax, name='search_ajax'),
    path('product/<int:id>/<slug:slug>/', views.product_detail_view, name='product_detail_view'),


]

