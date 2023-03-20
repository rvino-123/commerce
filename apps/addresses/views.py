from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from django.shortcuts import get_object_or_404

from .errors import (
    AddressCreateException,
    AddressUpdateException,
    AddressNotFoundException,
    AddressDeleteException,
    AddressDeletionFailedException,
)
from .models import Address
from .serializers import AddressSerializer, CreateAddressSerializer
from .renderers import AddressJSONRenderer


# Create your views here.
class UserAddressList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddressSerializer

    def get_queryset(self):
        user = self.request.user
        return Address.objects.filter(user=user).order_by("-default", "created_at")


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def get_address_api_view(request, address_id):
    try:
        address = Address.objects.get(id=address_id)
        serializer = AddressSerializer(address)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Address.DoesNotExist:
        raise AddressNotFoundException


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_address_api_view(request):
    data = request.data.dict()
    user = request.user
    data["user"] = user.pkid
    serializer = CreateAddressSerializer(data=data)
    if serializer.is_valid():
        if serializer.validated_data.get("user") != user:
            raise AddressCreateException
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([permissions.IsAuthenticated])
def update_address_api_view(request, address_id):
    try:
        address = Address.objects.get(id=address_id)
    except Address.DoesNotExist:
        raise AddressNotFoundException

    user = request.user
    if address.user != user:
        raise AddressUpdateException

    if request.method == "PUT":
        data = request.data
        serializer = AddressSerializer(address, data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def address_delete_api_view(request, address_id):
    try:
        address = Address.objects.get(id=address_id)
    except Address.DoesNotExist:
        raise AddressNotFoundException

    user = request.user
    if address.user != user:
        raise AddressDeleteException

    if request.method == "DELETE":
        delete_operation = address.delete()
        if delete_operation:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise AddressDeletionFailedException
