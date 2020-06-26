#from django.db import models

from __future__ import unicode_literals
from djongo import models


# Create your models here.

class Website(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    name = models.CharField(max_length=30)
    link = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
