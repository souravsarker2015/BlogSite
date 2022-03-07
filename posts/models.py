from django.db import models

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.CharField(max_length=2000)