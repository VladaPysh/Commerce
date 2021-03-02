from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return self.category

class Comment(models.Model):
    subject = models.CharField(max_length=64)
    comment = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=350)
    image = models.ImageField(default='default.png')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    date_created = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, default="None", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ManyToManyField(Comment, default=None)
    bid = models.ManyToManyField(Bid, default=None)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Watchlist(models.Model):
    listing = models.ManyToManyField(Listing)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
