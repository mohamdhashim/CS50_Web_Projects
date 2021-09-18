from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.expressions import Value


class User(AbstractUser):
    pass

class listings(models.Model):
    title = models.CharField(max_length=30)
    current_bid = models.IntegerField(null=True)
    start_bid = models.IntegerField(default=1)
    picture = models.FilePathField(default = '')


class comments(models.Model):
    user = models.CharField(max_length=30)
    title_id = models.ForeignKey(listings, on_delete=models.CASCADE,related_name='comments')
    text = models.CharField(max_length = 500)

class bids(models.Model):
    tile = models.ForeignKey(listings, on_delete = models.CASCADE, related_name ='bids')
    user = models.CharField(max_length = 30)
    value = models.IntegerField(null=False)

