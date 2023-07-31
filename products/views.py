from django.http import HttpRequest
from django.shortcuts import render, HttpResponse

from products.models import Product, Category


def index(request: HttpRequest):
    context = {
        'title': 'wazaap',
        'is_promotion': True,
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'products': Product.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'products/products.html', context)
