from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import *
from .forms import CreateListing, LeaveComment, Bid


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
        watchlist = Watchlist.objects.create(user=request.user)
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
            'form': CreateListing(),
            "categories": Category.objects.all()
        })

@login_required(login_url='/login')
def watch(request, listing_title):
    listing = Listing.objects.get(title=listing_title)
    if request.method == "POST":
        watchlist = Watchlist.objects.get(user=request.user)
        watchlist.listing.add(listing)
        messages.add_message(request, messages.SUCCESS, "Added to your watchlist")
        return redirect("item", listing_title=listing.title)

@login_required(login_url='/login')
def dont_watch(request, listing_title):
    listing = Listing.objects.get(title=listing_title)
    if request.method == "POST":
        watchlist = Watchlist.objects.get(user=request.user)
        watchlist.listing.remove(listing)
        messages.add_message(request, messages.SUCCESS, "Removed from your watchlist")
        return redirect("item", listing_title=listing.title)

@login_required(login_url='/login')
def watchlist(request):
    if not Watchlist.objects.filter(user=request.user).exists():
        watchlist = Watchlist.objects.create(user=request.user)
    watchlist = Watchlist.objects.get(user=request.user)
    return render(request, "auctions/watchlist.html", {
        "watchlist": watchlist,
        "categories": Category.objects.all()
        })

@login_required(login_url='/login')
def item(request, listing_title):
    #get item
    listing = Listing.objects.get(title=listing_title)
    if request.method == "POST":
        #get start bid value
        start_bid = listing.start_bid
        #get info from Bid form check if value is greater than starting price
        bid = float(request.POST['bid'])
        if bid > start_bid:
            bid = Bid(request.POST)
            if bid.is_valid():
                bid = bid.save(commit=False)
                bid.user = request.user
                bid.save()
                #save new value in listing bid instance
                listing.bid.add(bid)
                #overwrite start_bid with a new start value
                listing.start_bid = bid.bid
                listing.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.add_message(request, messages.WARNING, "Enter higher value")
            return redirect("item", listing_title=listing.title)
            
    return render(request, "auctions/item.html", {
        "listing": listing,
        "form": LeaveComment(),
        "bid": Bid(),
        "categories": Category.objects.all(),
        "watchlist": Watchlist.objects.get(user=request.user)
    })

@login_required(login_url='/login')
def auction_status(request, listing_title):
    listing = Listing.objects.get(title=listing_title)
    if request.method == "POST":
        listing.status = True
        listing.save()
    messages.add_message(request, messages.SUCCESS, "Auction closed")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/login')
def comment(request, listing_title):
    listing = Listing.objects.get(title=listing_title)
    if request.method == "POST":
        form = LeaveComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            listing.comment.add(comment)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            form = LeaveComment

@login_required(login_url='/login')
def delete_comment(request, comment_subject):
    comment = Comment.objects.get(subject=comment_subject)
    comment.delete()
    messages.add_message(request, messages.SUCCESS, "Comment deleted")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

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

def search(request):
    query = request.GET.get('q')
    listings = Listing.objects.all()
    for listing in listings:
        if query == listing.title:
            return redirect("item", listing_title = query)
        else:
            entries = []
            for listing in listings:
                if query.lower() in listing.title.lower():
                    entries.append(listing)
            if entries:
                return render(request, "auctions/search.html", {
                    "listings": entries
                })
            else:
                return render(request, "auctions/search.html", {
                    "message": "Nothing found"
                })