from .forms import CommentForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View
from .models import Post, Comment
from django.views.generic import DetailView, ListView
# Create your views here.


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = "-date"

    def get_queryset(self):
        return super().get_queryset()[:3]


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


class PostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        session = request.session
        return render(request, "blog/post-detail.html", {
            "post": post,
            "form": CommentForm(),
            "to_be_read": bool(session.get(f"read_later_slugs.{post.slug}")),
            "comments": Comment.objects.filter(post__slug=post.slug)
        })

    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        return render(request, "blog/post-detail.html", {
            "post": post,
            "form": form,
            "to_be_read": bool(request.session.get(f"read_later_slugs.{post.slug}")),
            "comments": Comment.objects.filter(post__slug=post.slug)
        })


class TagView(ListView):
    template_name = "blog/posts.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        query = super().get_queryset()
        return query.order_by("-date").filter(tags__caption=self.kwargs["tag_name"])
