from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'shop/index.html')


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
