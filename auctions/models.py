from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

category = [
    ('n', 'none'),
    ('f', 'food'),
    ('e', 'electronics'),
    ('c', 'clothes')
]

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=500)
    image = models.ImageField(default='default.png')
    start_bid = models.DecimalField(max_digits=6, decimal_places=2)
    date_created = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=1, choices=category, default=category[0][1])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title