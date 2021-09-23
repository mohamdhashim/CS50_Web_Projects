from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.expressions import Value


class User(AbstractUser):
    pass

class listings(models.Model):
    title = models.CharField(max_length=30)
    current_bid = models.IntegerField(null=True)
    start_bid = models.IntegerField(default=1)
    image = models.ImageField(blank=True , default = 'sabo.png')
    description = models.CharField(max_length=411, default = "No Describtion out there")

class comments(models.Model):
    user = models.CharField(max_length=30)
    title_id = models.ForeignKey(listings, on_delete=models.CASCADE,related_name='comments')
    text = models.CharField(max_length = 500)

class bids(models.Model):
    tile = models.ForeignKey(listings, on_delete = models.CASCADE, related_name ='bids')
    user = models.CharField(max_length = 30)
    value = models.IntegerField(null=False)

# panda = listings(title = "boo", current_bid = 45,start_bid = 10,picture = "/xss")
# mango = listings(title = "mango", current_bid = 55,start_bid = 20,picture = "/ss")
# mido = listings(title = "mido", current_bid = 5000,start_bid = 410,picture = "/s")
# sabona = listings(title = "sabo", current_bid = 450,start_bid = 10,picture = "/xsss")

# c1 = comments(user = "modo2020",title_id = listings(1), text = "iam very habby with this toy")
# c1.save()
# c2 = comments(user = "Hag Abd Elghafor", title_id = listings(2), text = "nice deal really")
# c2.save()
# c3 = comments(user = "odo200", title_id = listings(3), text = "nice man")
# c3.save()
# c4 = comments(user = "kokoo22", title_id = listings(1), text = "fuck seller")
# c4.save()
# c5 = comments(user = "manga15", title_id = listings(2), text = "nice slave")
# c5.save()
# c6 = comments(user = "mdo2020", title_id = listings(3), text = "iam very sad with this toy")
# c6.save()
# c7 = comments(user = "corj12", title_id = listings(1), text = "manga 3wesy gamda")
# c7.save()
# c8 = comments(user = "Abd Elwahab El-bor3y", title_id = listings(2), text = "Mr Hag u have no chance")
# c8.save()
