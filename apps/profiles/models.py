from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel

User = get_user_model()


class UserProfile(BaseModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(verbose_name="Phone Number", max_length=30)
    profile_photo = models.ImageField(verbose_name="Profile Photo", null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(verbose_name="Number of Reviews", null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
