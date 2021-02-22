from django.contrib import admin
from .models import Listing, Category, Watchlist, Comment

# Register your models here.

admin.site.register(Listing),
admin.site.register(Category),
admin.site.register(Watchlist),
admin.site.register(Comment)