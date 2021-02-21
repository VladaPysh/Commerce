from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("item/<str:listing_title>", views.item, name="item"),
    path("category/<str:category>", views.category, name="category")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
