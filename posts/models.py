import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

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

    class Meta:
        db_table = "Post"
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        def unique_code():
            # print(str(datetime.datetime.now().timestamp()))
            return str(datetime.datetime.now().timestamp() * pow(10, 6))

        if not self.slug:
            self.slug = slugify(self.title + unique_code())

        return super().save(*args, **kwargs)
