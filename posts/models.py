from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=500, error_messages={
        'max_length': "You Can't exceed more than 500 characters"
    })
    body = models.CharField(max_length=2000)
    published_on = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=300, unique=True, null=True, blank=True)
    status = models.CharField(max_length=500)
