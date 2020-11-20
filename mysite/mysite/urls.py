"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views as userviews
from order import views as orderviews
from wishlist import views as wishlistviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('user/', include('user.urls')),
    path('login/', userviews.loginform, name= 'loginform'),
    path('signout/', userviews.signout_page, name= 'signout'),
    path('signup/', userviews.signupform, name= 'signupform'),
    path('cart/', orderviews.cart, name= 'cart'),
    path('wishlist/', wishlistviews.wishlist, name= 'wishlist'),


]
