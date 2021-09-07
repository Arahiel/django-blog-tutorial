from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.base import View
from .models import Post
from django.views.generic import DetailView, ListView
# Create your views here.


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        query = super().get_queryset()
        return query.order_by("-date")[:3]


class PostsView(ListView):
    model = Post
    template_name = "blog/posts.html"
    context_object_name = "posts"
    ordering = "-date"


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
        context["to_be_read"] = bool(
            session.get(f"read_later_slugs.{post.slug}"))
        return context


class TagView(ListView):
    template_name = "blog/posts.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        query = super().get_queryset()
        return query.order_by("-date").filter(tags__caption=self.kwargs["tag_name"])
