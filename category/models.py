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