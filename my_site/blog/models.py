from datetime import datetime
from django.db import models
from django.db.models.fields.related import ManyToManyField

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
    image_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(default="", null=False, db_index=True)
    content = models.TextField(default="", max_length=1000)
    author = models.ForeignKey(Author, null=False, related_name="posts", on_delete=models.CASCADE)
    tags = ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.date_created:
            self.date_created = datetime.now()
        super().save(*args, **kwargs)
