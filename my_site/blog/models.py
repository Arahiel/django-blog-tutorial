from datetime import datetime
from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.TextField(max_length=255)
    image = models.ImageField(upload_to="images")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", null=False, unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, null=True, related_name="posts", on_delete=models.SET_NULL)
    tags = ManyToManyField(Tag, related_name="posts")
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    text = models.TextField(max_length=255)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text
