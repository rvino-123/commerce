from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from apps.common.serializers import BaseModelSerializer
from .models import Address


class AddressSerializer(BaseModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Address
        exclude = ["pkid", "user"]


class CreateAddressSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Address
        exclude = ["updated_at", "pkid"]
