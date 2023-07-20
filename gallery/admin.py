from django.contrib import admin
from gallery.models import Gallery, ArtPiece, Genre


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
class GalleryAdmin(admin.ModelAdmin):
    pass
