from django.shortcuts import get_object_or_404, render
from .models import Post
# Create your views here.


def index(request):
    posts_data = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": posts_data
    })


def posts(request):
    posts_data = Post.objects.all().order_by("-date")
    return render(request, "blog/posts.html", {
        "posts": posts_data
    })


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": post})


def tag(request, tag_name):
    posts_data = Post.objects.all().order_by("-date").filter(tags__caption=tag_name)
    return render(request, "blog/posts.html", {
        "posts": posts_data
    })
