from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.


def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides': nSlides,
    #           'range': range(1, nSlides), 'product': products}
    allProds = [[products, range(1, len(products)), nSlides], [
        products, range(1, len(products)), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("<h1>we are at contact</h1>")


def tracker(request):
    return HttpResponse("<h1>we are at tracker</h1>")


def search(request):
    return HttpResponse("<h1>we are at search</h1>")


def productView(request):
    return HttpResponse("<h1>we are at product View</h1>")


def checkout(request):
    return HttpResponse("<h1>we are at checkout</h1>")
