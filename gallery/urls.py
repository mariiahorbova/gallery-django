from django.urls import path
from .views import (
    index,
    UserListView,
    UserCreateView,
    UserDeleteView,
    UserDetailView,
    GenreListView,
    GenreCreateView,
    GenreDeleteView,
    GenreUpdateView,
    GalleryListView,
    GalleryCreateView,
    GalleryUpdateView,
    GalleryDeleteView,
    GalleryDetailView,
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
    path(
        "users/<int:pk>/",
        UserDetailView.as_view(),
        name="user-detail"
    ),

    path(
        "genres/",
        GenreListView.as_view(),
        name="genre-list",
    ),
    path(
        "genres/create/",
        GenreCreateView.as_view(),
        name="genre-create",
    ),
    path(
        "genres/<int:pk>/update/",
        GenreUpdateView.as_view(),
        name="genre-update"
    ),
    path(
        "genres/<int:pk>/delete/",
        GenreDeleteView.as_view(),
        name="genre-delete",
    ),

    path(
        "galleries/",
        GalleryListView.as_view(),
        name="gallery-list",
    ),
    path(
        "galleries/create/",
        GalleryCreateView.as_view(),
        name="gallery-create",
    ),
    path(
        "galleries/<int:pk>/update/",
        GalleryUpdateView.as_view(),
        name="gallery-update"
    ),
    path(
        "galleries/<int:pk>/delete/",
        GalleryDeleteView.as_view(),
        name="gallery-delete",
    ),
    path(
        "galleries/<int:pk>/",
        GalleryDetailView.as_view(),
        name="gallery-detail"
    ),
]


app_name = "gallery"
