from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(
        "cities_light.Country",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="galleries"
    )
    city = models.ForeignKey(
        "cities_light.City",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="galleries"
    )

    def __str__(self):
        return f"{self.name} ({self.country})"


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.name)


class ArtPiece(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.CharField(max_length=255)
    creation_date = models.DateField()
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

    def __str__(self):
        return f"{self.title} ({self.author})"


class User(AbstractUser):
    pseudonym = models.CharField(max_length=255, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    country = models.ForeignKey(
        "cities_light.Country",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users"
    )
    is_author = models.BooleanField(default=False)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("gallery:user-detail", kwargs={"pk": self.pk})
