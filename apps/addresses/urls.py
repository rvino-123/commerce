from django.urls import path
from .views import (
    UserAddressList,
    get_address_api_view,
    create_address_api_view,
    update_address_api_view,
    address_delete_api_view,
)


urlpatterns = [
    path("all/", UserAddressList.as_view(), name="get_all_addresses"),
    path(
        "<str:address_id>/details/",
        get_address_api_view,
        name="get_address_details",
    ),
    path("create/", create_address_api_view, name="create_address"),
    path("<str:address_id>/update/", update_address_api_view, name="update_address"),
    path("<str:address_id>/delete/", address_delete_api_view, name="delete_address"),
]
