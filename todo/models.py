from django.db import models

class Post(models.Model):
    body = models.CharField(max_length=200)