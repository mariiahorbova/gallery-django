from django.contrib import admin
from django.contrib.auth import get_user_model

from gallery.models import Gallery, ArtPiece, Genre


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(ArtPiece)
class ArtPieceAdmin(admin.ModelAdmin):
    list_display = [
            "title",
            "picture",
            "description",
            "creation_date",
            "author",
            "genre",
            "gallery"
        ]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
