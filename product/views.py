from django.shortcuts import render
from product.models import Product, Craft, Category
from photologue.models import Gallery

def index(request):
    products = Product.objects.all()
    covers = Gallery.objects.get(title='Cover Photos')
    return render(request, 'index.html', { "products" : products, "cover_photos" : covers })

def get_product(request,slug):
    product = Product.objects.get(product_slug = slug)
    return render(request, 'product.html', {'product':product})
