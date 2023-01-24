from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("auctions/watchlist", views.watchlist, name="watchlist"),
    path("auctions/<int:id>", views.listing_detail, name="detail"),
    path("auctions/<int:id>/comments", views.insert_comment, name="insert_comment"),
    path("auctions/<int:id>/bids", views.create_bid, name="create_bid"),
    path("auctions/<int:id>/watchlist", views.add_remove_watchlist, name="add_remove_watchlist"),
    path("auctions/create", views.create, name="create"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
