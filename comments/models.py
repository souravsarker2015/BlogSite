from django.db import models

from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=500, blank=True, null=True)
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    commented_by = models.CharField(max_length=50)

    class Meta:
        db_table = "Comment"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.body
