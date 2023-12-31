from PIL import Image as Im
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
import pyrebase
from gallery_mate.settings import firebase_config


firebase = pyrebase.initialize_app(firebase_config)
storage = firebase.storage()


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    country = CountryField(null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.country})"

    def get_absolute_url(self):
        return reverse("gallery:gallery-detail", kwargs={"pk": self.pk})


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return str(self.name)


class ArtPiece(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.ImageField(upload_to="pictures")
    creation_date = models.DateField()
    firebase_image_url = models.URLField(blank=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="art_pieces"
    )
    genre = models.ForeignKey(
        to=Genre,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="art_pieces"
    )
    gallery = models.ForeignKey(
        to=Gallery,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="art_pieces"
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} ({self.author})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Im.open(self.picture.path)
        img.save(self.picture.path)

        storage.child("art_pieces/{0}".format(
            self.picture.name
        )).put(self.picture.path)
        self.firebase_image_url = storage.child(
            "art_pieces/{0}".format(self.picture.name)
        ).get_url(None)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("gallery:art-piece-detail", kwargs={"pk": self.pk})


class User(AbstractUser):
    pseudonym = models.CharField(max_length=255, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    is_author = models.BooleanField(default=False)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["username"]

    def __str__(self):
        user_string = f"{self.username}"
        if self.first_name and self.last_name:
            user_string += f"({self.first_name} {self.last_name})"

        return user_string

    def get_absolute_url(self):
        return reverse("gallery:user-detail", kwargs={"pk": self.pk})
