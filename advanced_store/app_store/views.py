from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    context = {
        "title": "Phone Stock"
    }
    return render(request, 'app_store/index.html', context)


def products(request, category_id=None, page=1):
    if category_id is None:
        products_all = Product.objects.all()
    else:
        products_all = Product.objects.filter(category=category_id)

    categories_all = ProductCategory.objects.all()

    paginator = Paginator(products_all, 3)
    products_paginator = paginator.page(page)
    products_all = products_paginator

    context = {
        "title": "Каталог",
        'products': products_all,
        'categories': categories_all
    }
    return render(request, 'app_store/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_del(request, id):
    basket = Basket.objects.get(id=id)

    if basket.quantity > 1:
        basket.quantity -= 1
        basket.save()
    else:
        Basket.objects.get(id=id).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

