from django.shortcuts import render

# Create your views here.
"""
Updating Data in the database
for comment in Comment.objects.all():
... print(comment.id)
>>> cmt2 = Comment.objects.get(id=......)
>>> cmt2.post
<Post: My Educational Post 2>
>>> cmt2.post = p1
>>> cmt2.save()
cmt2.post
<Post: My Educational Post 1>
"""