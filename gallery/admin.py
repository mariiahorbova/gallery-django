from django.contrib import admin
from gallery.models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass
