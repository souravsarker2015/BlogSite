from django.contrib.auth.models import User
from django.db import models
from category.models import Category


class Post(models.Model):
    POST_STATUS_CHOICES = (
        ('P', 'Pending for approval'),
        ('R', 'Rejected'),
        ('A', 'Approved'),
        ('B', 'Blocked'),
    )

    title = models.CharField(max_length=500, error_messages={
        'max_length': "You Can't exceed more than 500 characters"
    })
    body = models.CharField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, blank=True)
    published_on = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    status = models.CharField(max_length=1, choices=POST_STATUS_CHOICES, default='P')




