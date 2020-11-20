from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Cart, CartForm, Order, OrderProduct, ShippingForm
from django.contrib.auth.decorators import login_required
from wishlist.models import WishlistCart
from user.models import Profile
from django.utils.crypto import get_random_string
from product.models import Product

# Create your views here.

def index(request):
    return HttpResponse("my order page")


@login_required(login_url = '/login')
def addtocart(request,id):
    current_user = request.user 

    checkproduct = Cart.objects.filter(product_id = id)


    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            if checkproduct:
                cart_obj = Cart.objects.get(product_id= id)
                cart_obj.quantity += form.cleaned_data['quantity']
                cart_obj.save()
            else:
                cart_obj = Cart()
                cart_obj.user_id = current_user.id 
                cart_obj.product_id = id
                cart_obj.quantity = form.cleaned_data['quantity']
                cart_obj.save()
            messages.success(request, "Product added to Cart")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        if checkproduct:
            cart_obj = Cart.objects.get(product_id= id)
            cart_obj.quantity += 1
            cart_obj.save()
        else:
            cart_obj = Cart()
            cart_obj.user_id = current_user.id
            cart_obj.product_id = id
            cart_obj.quantity = 1
            cart_obj.save()
        messages.success(request, "Product added to Cart")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  


@login_required(login_url = '/login')
def cart(request):
    current_user = request.user
    cart = Cart.objects.filter(user_id = current_user.id)
    total = 0
    shipping = 80
    for x in cart:
        subtotal =  x.product.price * x.quantity
        total    = total + subtotal

    net = total + shipping
    context = { 
        'cart'      : cart,
        'total'     : total,
        'shipping'  : shipping,
        'net'       : net,

    }
    return render(request, 'cart.html', context)

@login_required(login_url = '/login')
def removecart(request, id):
    Cart.objects.filter(id = id).delete()
    context = {

    }
    return HttpResponseRedirect("/cart")

@login_required(login_url = '/login')
def orderproduct(request):
    current_user = request.user
    billing_form = ShippingForm()
    profile = Profile.objects.get(user_id = current_user.id)
    cart = Cart.objects.filter(user_id = current_user.id)
    total = 0
    shipping = 80
    for kart in cart:
        subtotal = kart.price * kart.quantity
        total    = total + subtotal

    net = total + shipping

    if request.method == 'POST':
        billing_form = ShippingForm(request.POST)
        if billing_form.is_valid():
            billing_info               = Order()
            billing_info.first_name    = billing_form.cleaned_data['first_name']
            billing_info.last_name     = billing_form.cleaned_data['last_name']
            billing_info.email         = billing_form.cleaned_data['email']
            billing_info.contact       = billing_form.cleaned_data['contact']
            billing_info.pincode       = billing_form.cleaned_data['pincode']
            billing_info.address       = billing_form.cleaned_data['address']
            billing_info.landmark      = billing_form.cleaned_data['landmark']
            billing_info.city          = billing_form.cleaned_data['city']
            billing_info.state         = billing_form.cleaned_data['state']
            billing_info.total         = billing_form.cleaned_data['total']
            billing_info.cname         = billing_form.cleaned_data['cname']
            billing_info.ccnum         = billing_form.cleaned_data['ccnum']
            billing_info.expmonth      = billing_form.cleaned_data['expmonth']
            billing_info.expyear       = billing_form.cleaned_data['expyear']
            billing_info.cvv           = billing_form.cleaned_data['cvv']
            billing_info.user_id       = current_user.id
            code                       = get_random_string(length=14)
            billing_info.ordercode     = code 
            billing_info.save()
            
            for orders in cart:
                order_obj               = OrderProduct()
                order_obj.user_id       = current_user.id
                order_obj.product_id    = orders.product_id
                order_obj.order_id      = billing_info.id       # give us the order id
                order_obj.price         = orders.price
                order_obj.quantity      = orders.quantity
                order_obj.amount        = orders.amount
                order_obj.save()

                # product = Product.objects.get(id= orders.product_id) 
                # product.quantity -= orders.quantity                        # decreases the quantity of item from database after completion
                # product.save()

            Cart.objects.filter(user_id = current_user.id).delete()
            request.session['cart_items'] = 0
            messages.success(request, "Your order has been placed. Thank you!!")
            context = { 
                'code'      : code,
                'net'      : net,
            }
            return render(request, 'ordercomplete.html', context)
        else: 
            messages.warning(request, billing_form.errors)
            return HttpResponseRedirect("/order/billing")
    
    context = {
        'profile'       : profile,
        'net'           : net,
        'billing_form'  : billing_form,
        'cart'          : cart    
    }
    return render(request, 'billing.html', context)