from django.urls import path
from .views import (
    index,
    UserListView,
    UserCreateView,
    UserDeleteView,
    UserDetailView,

)


urlpatterns = [
    path("", index, name="index"),
    path(
        "users/",
        UserListView.as_view(),
        name="user-list",
    ),
    path(
        "users/create/",
        UserCreateView.as_view(),
        name="user-create",
    ),
    path(
        "users/<int:pk>/delete/",
        UserDeleteView.as_view(),
        name="user-delete",
    ),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
]


app_name = "gallery"
