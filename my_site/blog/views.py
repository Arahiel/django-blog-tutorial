from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/post.html", {
        "page_title": "All posts"
    })

def post(request, slug):
    return render(request, "blog/post.html", {
        "page_title": "Post title"
    })