from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from .views import (
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
    ArtPieceListView,
    ArtPieceCreateView,
    ArtPieceDeleteView,
    ArtPieceDetailView,
    ArtPieceUpdateView
)


urlpatterns = [
    path(
        "",
        RedirectView.as_view(
            url=reverse_lazy("gallery:art-piece-list")
        )
    ),
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

    path(
        "art-pieces/",
        ArtPieceListView.as_view(),
        name="art-piece-list",
    ),

    path(
        "art-pieces/<int:pk>/update/",
        ArtPieceUpdateView.as_view(),
        name="art-piece-update",
    ),
    path(
        "art-pieces/create/",
        ArtPieceCreateView.as_view(),
        name="art-piece-create",
    ),
    path(
        "art-pieces/<int:pk>/delete/",
        ArtPieceDeleteView.as_view(),
        name="art-piece-delete",
    ),
    path(
        "art-pieces/<int:pk>/",
        ArtPieceDetailView.as_view(),
        name="art-piece-detail"
    ),
]

app_name = "gallery"
