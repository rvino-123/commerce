from django.db import models
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel

User = get_user_model()


class Address(BaseModel):
    user = models.ForeignKey(User, related_name="addresses", on_delete=models.CASCADE)
    address_line = models.TextField(blank=False, null=False)
    city = models.CharField(max_length=180, blank=False, null=False)
    country = CountryField(blank=False, null=False)
    post_code = models.CharField(max_length=50, blank=False, null=False)
    phone_number = PhoneNumberField(max_length=30)
    default = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return f"Address {self.id}"
