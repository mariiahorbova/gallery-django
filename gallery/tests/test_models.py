from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from gallery.models import ArtPiece, Gallery, Genre


class ArtPieceModelTestCase(TestCase):
    title = "The Starry Night"
    description = "Van Gogh in asylum"
    picture = "pictures/icon.png"
    creation_date = "2020-04-21"

    @classmethod
    def setUpTestData(cls):
        art_piece = ArtPiece(
            title=cls.title,
            description=cls.description,
            picture=cls.picture,
            creation_date=cls.creation_date,
        )
        art_piece.save()

    def test_art_piece_str(self):
        art_piece = ArtPiece.objects.get(id=1)

        self.assertEqual(
            str(art_piece),
            f"{art_piece.title} ({art_piece.author})"
        )

    def test_get_absolute_url(self):
        art_piece = ArtPiece.objects.get(id=1)
        self.assertEquals(
            art_piece.get_absolute_url(),
            reverse(
                "gallery:art-piece-detail",
                kwargs={"pk": art_piece.pk}
            )
        )


class GenreModelTestCase(TestCase):
    name = "Art neuvo"

    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(
            name=cls.name,
        )

    def test_genre_str(self):
        genre = Genre.objects.get(id=1)

        self.assertEqual(
            str(genre),
            f"{genre.name}"
        )


class GalleryModelTestCase(TestCase):
    name = "Art neuvo"
    country = None

    @classmethod
    def setUpTestData(cls):
        Gallery.objects.create(
            name=cls.name,
            country=cls.country
        )

    def test_genre_str(self):
        gallery = Gallery.objects.get(id=1)

        self.assertEqual(
            str(gallery),
            f"{self.name} ({self.country})"
        )

    def test_get_absolute_url(self):
        gallery = Gallery.objects.get(id=1)
        self.assertEquals(
            gallery.get_absolute_url(),
            reverse(
                "gallery:gallery-detail",
                kwargs={"pk": gallery.pk}
            )
        )


class UserModelTestCase(TestCase):
    username = "ria"
    pseudonym = "maria"
    is_author = True
    password1 = "1Qazxrw@"
    first_name = "Mariia"
    last_name = "Roma"

    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create(
            username=cls.username,
            pseudonym=cls.pseudonym,
            is_author=cls.is_author,
            first_name=cls.first_name,
            last_name=cls.last_name,
        )
        user.set_password(cls.password1)

    def test_user_str(self):
        user = get_user_model().objects.get(id=1)

        self.assertEqual(
            str(user),
            f"{self.username} ({self.first_name} {self.last_name})"
        )

    def test_get_absolute_url(self):
        user = get_user_model().objects.get(id=1)
        self.assertEquals(
            user.get_absolute_url(),
            reverse(
                "gallery:user-detail",
                kwargs={"pk": user.pk}
            )
        )

    def test_model_verbose_name(self):
        model_verbose_name = "user"
        model_verbose_name_plural = "users"

        self.assertEqual(
            get_user_model()._meta.verbose_name,
            model_verbose_name
        )
        self.assertEqual(
            get_user_model()._meta.verbose_name_plural,
            model_verbose_name_plural
        )
