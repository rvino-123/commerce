from django.urls import path
from .views import GetUserProfileAPIView, UpdateProfileAPIView, ListUserProfilesAPIView

urlpatterns = [
    path("me/", GetUserProfileAPIView.as_view(), name="view_profile"),
    path(
        "update/<str:username>/", UpdateProfileAPIView.as_view(), name="update_profile"
    ),
    path("all/", ListUserProfilesAPIView.as_view(), name="all_profiles"),
]
