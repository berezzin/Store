from django.http import HttpRequest
from django.shortcuts import render, HttpResponse


def index(request: HttpRequest):
    return render(request, 'products/index.html', {'title': 'My products title'})
