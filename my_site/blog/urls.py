from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/add-read_later", views.AddReadLaterView.as_view(), name="add-read-later"),
    path("posts/remove-read-later", views.RemoveReadLaterView.as_view(), name="remove-read-later"),
    path("posts/<slug:slug>", views.PostView.as_view(), name="post-detail-page"),
    path("tag/<str:tag_name>", views.tag, name="tag-page")
]
