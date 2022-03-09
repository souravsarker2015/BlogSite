from django.db import models

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=500,error_messages=
    {
        'max_length':"You Can't exceed more than 500 characters"
    })
    body = models.CharField(max_length=2000)
    published_on = models.DateTimeField()
    last_updated_on = models.DateTimeField()
    slug = models.SlugField()
    status = models.CharField()

