from django.shortcuts import render
from .models import Product2


def index(request):
    products = Product2.objects.all()  # it return all the products in a database
    return render(request, 'index.html', {'products': products})  # we use the function (render) to render a template
