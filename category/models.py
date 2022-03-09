from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    CATEGORY_CHOICES = (
        ('P', 'Pending for approval'),
        ('R', 'Rejected'),
        ('A', 'Approved'),
        ('B', 'Blocked'),
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=5000, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default='P')
