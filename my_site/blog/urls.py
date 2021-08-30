from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post, name="post-detail-page"),
    path("tag/<str:tag_name>", views.tag, name="tag-page")
]
