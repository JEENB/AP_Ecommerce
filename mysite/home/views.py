from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from product.models import Product, Images, Review
from .forms import Search
import random
import json
# Create your views here.

def home_page_view(request):
    popular_product = Product.objects.all().order_by('?')[:8]
    phones          = Product.objects.filter(category='Smart').order_by('?')[:4]
    lap             = Product.objects.filter(category='Laptop').order_by('?')[:8]
    com             = Product.objects.filter(category='Computer').order_by('?')[:4]
    access          = Product.objects.filter(category='Accessories').order_by('?')[:8]

    context = {
        'popular_product' : popular_product,
        'phones'          : phones,
        'lap'             : lap,
        'com'             : com,
        'access'          : access,
    }
    return render(request, 'index.html',context)


def computers_page_view(request):
    com_page    = Product.objects.filter(category='Computer').order_by('?')[:]
    context = {
        'com_page': com_page,
    }
    return render(request, 'computers.html',context)

def laptopss_page_view(request):
    lap_page     = Product.objects.filter(category='Laptop').order_by('?')[:]
    context = {
        'lap_page': lap_page,
    }
    return render(request, 'laptops.html',context)
    
def accessories_page_view(request):
    acces_page     = Product.objects.filter(category='Accessories').order_by('?')[:]
    context = {
        'acces_page': acces_page,
    }
    return render(request, 'accessories.html',context)

def phones_page_view(request):
    phones_page     = Product.objects.filter(category='Smart').order_by('?')[:]
    context = {
        'phones_page': phones_page,
    }
    return render(request, 'phones.html',context)

def about_page_view(request):
    context={}
    return render(request, 'about.html', context)


def contact_page_view(request):
    context = {}
    return render(request, 'contact.html', context)


def terms_page_view(request):
    context={}
    return render(request, 'terms.html', context)



def product_detail_view(request, slug, id):
    product     = Product.objects.get(pk = id)
    img         = Images.objects.filter(product_id= id)
    more_like   = Product.objects.all().order_by('?')[:4]
    reviews     = Review.objects.filter(product_id = id).order_by('?')[:4]
    context     = {
        'product'   : product,
        'more_like' : more_like,
        'img'       : img,
        'reviews'   : reviews
    }
    return render(request, 'product_detail.html', context)



def search_page_view(request):
    if request.method == "POST":
        form = Search(request.POST)
        if form.is_valid():
            query          = form.cleaned_data['query']
            search_product = Product.objects.filter(title__icontains=query)
            context={
                'search_product': search_product,
                'query': query
                    }
            return render(request, 'search.html', context)



#====================================================================
#auto search; copied from http://www.lalicode.com/post/5/ #citation
def search_ajax(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    products = Product.objects.filter(title__icontains=q)
    results = []
    for smart in products:
      product_json = {}
      product_json = smart.title 
      results.append(product_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)  
#====================================================================


