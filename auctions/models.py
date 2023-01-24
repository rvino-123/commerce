from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def get_watchlist_count(self):
        return len(self.listings.all())


class Category(models.Model):
    title = models.CharField(max_length=50)


class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    starting_bid = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    image = models.ImageField()
    watchers = models.ManyToManyField(User, related_name="listings")

    def get_highest_bid(self):
       if len(self.bid_set.all()) > 0:
            return self.bid_set.order_by('-price')[0]
       return None


class Bid(models.Model):
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if (self.listing.get_highest_bid() and self.listing.get_highest_bid().price \
            < float(self.price)) or not self.listing.get_highest_bid():
            super(Bid, self).save(*args, **kwargs)
        else:
            raise Exception("Bid must be higher than current bid")

class Comment(models.Model):
    description = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)


