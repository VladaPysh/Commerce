from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("item/<str:listing_title>", views.item, name="item"),
    path("category/<str:category_name>", views.category, name="category"),
    path("watch/<str:listing_title>", views.watch, name="watch"),
    path("dont_watch/<str:listing_title>", views.dont_watch, name="dont_watch"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("comment/<str:listing_title>", views.comment, name="comment"),
    path("delete/<str:comment_subject>", views.delete_comment, name="delete_comment")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
