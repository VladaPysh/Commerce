from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import User, Listing, Category, Watchlist
from .forms import CreateListing


def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        "listings": listings,
        "categories": Category.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required(login_url='/login')
def create(request):
    if request.method == 'POST':
        form = CreateListing(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()
            
            return redirect("item", listing_title = listing.title)
        else:
            form = CreateListing
    
    return render(request, "auctions/create.html", {
            'form': CreateListing()
        })

@login_required(login_url='/login')
def watch(request):
    listings = Watchlist.objects.all()
    return render(request, "auctions/watchlist.html", {
        "listings": listings
    })

@login_required(login_url='/login')
def item(request, listing_title):
    listing = Listing.objects.get(title=listing_title)
    return render(request, "auctions/item.html", {
        "listing": listing
    })

def category(request, category_name):
    #get list of categories
    category = Category.objects.get(category=category_name)
    #get listings where category field matches category selected
    listing_category = Listing.objects.filter(category=category)
    #return template providing category names and listings
    return render(request, "auctions/category.html", {
        "category": category.category,
        "listings": listing_category,
        "categories": Category.objects.all()
    })
