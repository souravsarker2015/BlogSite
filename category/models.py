from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    CATEGORY_CHOICES = (
        ('P', 'Pending for approval'),
        ('R', 'Rejected'),
        ('A', 'Approved'),
        ('B', 'Blocked'),
    )
    name = models.CharField("Category Name", max_length=200, unique=True)
    description = models.TextField(max_length=5000, blank=True, null=True, verbose_name="Category Descriptions")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Created By")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(verbose_name="Category Status", max_length=1, choices=CATEGORY_CHOICES, default='P')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


"""
from posts.models import Post
for post in Post.objects.all():
    print(post.id)
    
3
4
5
6
p1=Post.objects.get(id=3)
p1
<Post: My Educational Post 1>

Model Manager
➢ A Manager is the interface through which database query operations are provided
to Django models.
➢ At least one Manager exists for every model in a Django application.
➢ Django adds a Manager with the name objects to every Django model class.
➢ We can also create our own model manager or modify the functionality of existing
model manager
"""
