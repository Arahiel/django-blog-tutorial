from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.base import View
from .models import Post
from django.views.generic import DetailView
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


class AddReadLaterView(View):
    def post(self, request):
        slug = request.POST["read_later_slug"]
        request.session[f"read_later_slugs.{slug}"] = True
        return HttpResponseRedirect(reverse("post-detail-page", args=(slug,)))

class RemoveReadLaterView(View):
    def post(self, request):
        slug = request.POST["read_later_slug"]
        request.session[f"read_later_slugs.{slug}"] = False
        return HttpResponseRedirect(reverse("post-detail-page", args=(slug,)))


class PostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session = self.request.session
        post = self.object
        context["to_be_read"] = bool(session.get(f"read_later_slugs.{post.slug}"))
        return context


def tag(request, tag_name):
    posts_data = Post.objects.all().order_by(
        "-date").filter(tags__caption=tag_name)
    return render(request, "blog/posts.html", {
        "posts": posts_data
    })
