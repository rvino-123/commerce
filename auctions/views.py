from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Category, Comment, Bid


def index(request):
    listings = Listing.objects.filter(active=True)
    return render(request, "auctions/index.html", {
        "listings": listings
    })


def listing_detail(request, id):
    listing = Listing.objects.filter(id=id)[0]
    if not listing:
        raise Http404()

    highest_bid = listing.get_highest_bid()
    comments = listing.comment_set.all()


    return render(request, "auctions/detail.html", {
        "listing": listing,
        "comments": comments,
        "highest_bid": highest_bid
    })

@login_required
def create(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        data = request.POST.dict()
        data["category"] = Category.objects.get(id=data["category"])
        data["user_id"] = User.objects.get(id=data["user_id"])
        listing = Listing(title=data.get("title"),
                            description=data.get("description"),
                            category = data.get("category"),
                            starting_bid = data.get("starting_bid"),
                            user_id = user
                        )
        listing.save()
        return redirect("/")
    categories = Category.objects.all()
    return render(request, "auctions/create.html", {
        "categories": categories
    })

# Bids
# POST /auction/<id>/bids
def create_bid(request, id):
    # If method is POST
    if request.method == "POST":
        # Get post data
        data = request.POST
        # Get user from request
        user = User.objects.get(id=request.user.id)
        # get auction from form data
        auction = Listing.objects.get(id=id)
        # instantiate bid and save
        print(data["price"])
        bid = Bid(price=data["price"], user=user, listing=auction)
        print(bid)
        try:
            bid.save()
        except Exception as e:
            print(e)
        finally:
            return redirect(reverse("detail", args=[id]))

# POST /auction/<id>/comments
def insert_comment(request, id):
    if request.method == "POST":
        data = request.POST
        auction = Listing.objects.get(id=id)
        user = User.objects.get(id=request.user.id)
        comment = Comment(user_id=user, listing_id=auction, 
            description=data.get("description"))
        comment.save()
        return redirect(reverse("detail", args=[id]))

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


# errors
def my_custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})
