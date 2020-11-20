from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from product.models import Review, ReviewForm
# Create your views here.


def addreview(request, id):
    geturl = request.META.get('HTTP_REFERER')
    current_user = request.user 

    if request.method == 'POST':
        reviewform = ReviewForm(request.POST)
        if reviewform.is_valid():
            rev             = Review()
            rev.comment     = reviewform.cleaned_data['comment']
            rev.rate        = reviewform.cleaned_data['rate']
            rev.user_id     = current_user.id 
            rev.product_id  = id
            rev.save()
            messages.success(request, "Your review has been sent. Thank You!!")
            return HttpResponseRedirect(geturl)

    return HttpResponseRedirect(geturl)
