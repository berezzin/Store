from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render, HttpResponseRedirect

from products.models import Product, Category, Basket


def index(request: HttpRequest):
    context = {
        'title': 'wazaap',
        'is_promotion': True,
    }
    return render(request, 'products/index.html', context)


def products(request, category_id: int = 0, page_number=1):
    products_list = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    paginator = Paginator(products_list, per_page=3)
    products_paginator = paginator.page(page_number)

    context = {
        'products': products_paginator,
        'categories': Category.objects.all(),
        'category_id': category_id
    }
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
