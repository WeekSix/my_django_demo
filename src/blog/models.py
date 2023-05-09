from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
    # picture = models.ImageField()


class Comment(models.Model):
    comment = models.TextField()


class Author(models.Model):
    name = models.TextField()
