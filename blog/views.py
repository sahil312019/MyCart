from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost


def index(request):
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request, 'blog/index.html', {'myposts': myposts})


def blogpost(request):
    return render(request, "blog/blogpost.html")
