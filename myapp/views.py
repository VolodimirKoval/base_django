from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    context = {
        'title': 'Main Page',
        'products': products
    }
   
    return render(request, 'myapp/index.html', context=context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'title': product.name,
        'product': product,
    }
    return render(request, 'myapp/product_detail.html', context=context)

