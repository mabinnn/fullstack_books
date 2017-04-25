from __future__ import unicode_literals
from django.db import models

class Book(models.Model):
    title =  models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    category = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)