from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.


def index(request):
    products = Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("<h1>we are at contact</h1>")


def tracker(request):
    return HttpResponse("<h1>we are at tracker</h1>")


def search(request):
    return HttpResponse("<h1>we are at search</h1>")


def productView(request, myid):
    product = Product.objects.filter(id=myid)
    # print(product)
    # id = myid will make sure the chosen item is only present in query set which we are accessing using 0th index
    return render(request, "shop/prodView.html", {'product': product[0]})


def checkout(request):
    return HttpResponse("<h1>we are at checkout</h1>")
