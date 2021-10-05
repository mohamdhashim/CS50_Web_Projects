from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.expressions import Value


class User(AbstractUser):
    pass

class Listings(models.Model):
    title = models.CharField(max_length=30)
    current_bid = models.IntegerField(default=1)
    start_bid = models.IntegerField(default=1)
    image = models.ImageField(blank=True , default = 'sabo.png' )
    description = models.CharField(max_length=411, default = "No Describtion out there")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name ="listings")

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ="comments")
    title_id = models.ForeignKey(Listings, on_delete=models.CASCADE,related_name='comments')
    text = models.CharField(max_length = 500)


class Bids(models.Model):
    tile = models.ForeignKey(Listings, on_delete = models.CASCADE, related_name ='bids')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ="bids")
    value = models.IntegerField(null=False)


class Watch_List(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name ='list')
    title = models.ForeignKey(Listings, on_delete = models.CASCADE, related_name ='viewers')
    