from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from datetime import date
# Create your views here.

posts_data = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Sebastian",
        "date": date(2021, 8, 23),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """Mountains - Lorem, ipsum dolor sit amet consectetur adipisicing elit. Obcaecati esse possimus praesentium quaerat velit
                    dolorem ab doloremque facilis ut eaque, cupiditate fuga perspiciatis aliquid voluptatum temporibus at ea libero.
                    Magni.
                    
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Obcaecati esse possimus praesentium quaerat velit
                    dolorem ab doloremque facilis ut eaque, cupiditate fuga perspiciatis aliquid voluptatum temporibus at ea libero.
                    Magni.
                    
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Obcaecati esse possimus praesentium quaerat velit
                    dolorem ab doloremque facilis ut eaque, cupiditate fuga perspiciatis aliquid voluptatum temporibus at ea libero.
                    Magni."""
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Sebastian",
        "date": date(2020, 1, 22),
        "title": "Nature At Its Best",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """Woods - Lorem, ipsum dolor sit amet consectetur adipisicing elit. Obcaecati esse possimus praesentium quaerat velit
                    dolorem ab doloremque facilis ut eaque, cupiditate fuga perspiciatis aliquid voluptatum temporibus at ea libero.
                    Magni.
                    
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Obcaecati esse possimus praesentium quaerat velit
                    dolorem ab doloremque facilis ut eaque, cupiditate fuga perspiciatis aliquid voluptatum temporibus at ea libero.
                    Magni.
                    
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Obcaecati esse possimus praesentium quaerat velit
                    dolorem ab doloremque facilis ut eaque, cupiditate fuga perspiciatis aliquid voluptatum temporibus at ea libero.
                    Magni."""
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Sebastian",
        "date": date(2021, 6, 1),
        "title": "Programming Is Great!",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """Programming - Lorem, ipsum dolor sit amet consectetur adipisicing elit. Obcaecati esse possimus praesentium quaerat velit
                    dolorem ab doloremque facilis ut eaque, cupiditate fuga perspiciatis aliquid voluptatum temporibus at ea libero.
                    Magni.
                    
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Obcaecati esse possimus praesentium quaerat velit
                    dolorem ab doloremque facilis ut eaque, cupiditate fuga perspiciatis aliquid voluptatum temporibus at ea libero.
                    Magni.
                    
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Obcaecati esse possimus praesentium quaerat velit
                    dolorem ab doloremque facilis ut eaque, cupiditate fuga perspiciatis aliquid voluptatum temporibus at ea libero.
                    Magni."""
    },
    {
        "slug": "programming-is-fun-2",
        "image": "coding.jpg",
        "author": "Sebastian",
        "date": date(2021, 6, 14),
        "title": "Programming Is Great 2!",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """Programming 2 - Lorem, ipsum dolor sit amet consectetur adipisicing elit. Obcaecati esse possimus praesentium quaerat velit
                    dolorem ab doloremque facilis ut eaque, cupiditate fuga perspiciatis aliquid voluptatum temporibus at ea libero.
                    Magni.
                    
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Obcaecati esse possimus praesentium quaerat velit
                    dolorem ab doloremque facilis ut eaque, cupiditate fuga perspiciatis aliquid voluptatum temporibus at ea libero.
                    Magni.
                    
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Obcaecati esse possimus praesentium quaerat velit
                    dolorem ab doloremque facilis ut eaque, cupiditate fuga perspiciatis aliquid voluptatum temporibus at ea libero.
                    Magni."""
    }
]


def index(request):
    sorted_posts = sorted(posts_data, key=lambda post: post["date"])
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    sorted_posts = sorted(posts_data, key=lambda post: post["date"])
    return render(request, "blog/posts.html", {
        "posts": sorted_posts
    })


def post(request, slug):
    try:
        identified_post = next(
            post for post in posts_data if post["slug"] == slug)
        return render(request, "blog/post-detail.html", {
            "post": identified_post
        })
    except:
        raise Http404
