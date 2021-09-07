from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="starting-page"),
    path("posts", views.PostsView.as_view(), name="posts-page"),
    path("posts/add-read_later", views.AddReadLaterView.as_view(), name="add-read-later"),
    path("posts/remove-read-later", views.RemoveReadLaterView.as_view(), name="remove-read-later"),
    path("posts/add-comment", views.AddCommentView.as_view(), name="add-comment"),
    path("posts/<slug:slug>", views.PostView.as_view(), name="post-detail-page"),
    path("tag/<str:tag_name>", views.TagView.as_view(), name="tag-page")
]
