import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from gallery.models import ArtPiece, Genre, Gallery

GALLERY_LIST_URL = reverse("gallery:gallery-list")
ART_PIECE_LIST_URL = reverse("gallery:art-piece-list")
GENRE_LIST_URL = reverse("gallery:genre-list")
USER_LIST_URL = reverse("gallery:user-list")


class PrivateArtPieceTest(TestCase):
    def setUp(self):
        for i in range(10):
            genre = Genre.objects.create(
                name=f"genre_name_{i}",
            )
            art_piece = ArtPiece(
                title=f"test_{i}",
                genre=genre,
                picture=f"pictures/icon.png",
                creation_date=datetime.date(2020, 4, 21)
            )
            art_piece.save()

        user = get_user_model().objects.create(
            username="usernametest",
            password="1Qazxrw@",
            pseudonym="ria"
        )
        self.client.force_login(user)

    def test_all_art_pieces(self):
        paginated_by = 6
        response = self.client.get(ART_PIECE_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["art_piece_list"]),
            list(ArtPiece.objects.all())[:paginated_by]
        )


class PublicUserTest(TestCase):
    def test_login_required(self):
        response = self.client.get(USER_LIST_URL)

        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(
            response,
            f"/accounts/login/?next={USER_LIST_URL}"
        )


class PrivateUserTest(TestCase):
    def setUp(self):
        for i in range(10):
            get_user_model().objects.create(
                username=f"test_{i}",
                password=f"test_password{i}!",
                pseudonym=f"test_pseudo{i}"
            )

        user = get_user_model().objects.create(
            username="riauser",
            password="r1@useR",
            pseudonym=f"ria"
        )
        self.client.force_login(user)

    def test_all_users(self):
        paginated_by = 10
        response = self.client.get(USER_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["user_list"]),
            list(get_user_model().objects.all())[:paginated_by]
        )

    def test_search_user_by_username(self):
        searched_username = "test_5"
        response = self.client.get(
            USER_LIST_URL,
            {"username": searched_username}
        )
        print(response.context["user_list"])

        self.assertEqual(
            response.context["user_list"][0],
            get_user_model().objects.get(username=searched_username)
        )

    def test_search_user_by_extra_long_username(self):
        searched_name = "a" * 256
        response = self.client.get(
            USER_LIST_URL,
            {"username": searched_name}
        )

        self.assertEqual(
            list(response.context["user_list"]),
            list(get_user_model().objects.all().exclude(username="riauser"))

        )


class PublicGalleryTest(TestCase):
    def test_login_required(self):
        response = self.client.get(GALLERY_LIST_URL)

        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(
            response,
            f"/accounts/login/?next={GALLERY_LIST_URL}"
        )


class PrivateGalleryTest(TestCase):
    def setUp(self):
        for i in range(10):
            Gallery.objects.create(
                name=f"test_{i}"
            )

        user = get_user_model().objects.create(
            username="riauser",
            password="r1@useR",
            pseudonym=f"ria"
        )
        self.client.force_login(user)

    def test_all_galleries(self):
        paginated_by = 10
        response = self.client.get(GALLERY_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["gallery_list"]),
            list(Gallery.objects.all())[:paginated_by]
        )

    def test_search_gallery_by_name(self):
        searched_name = "test_7"
        response = self.client.get(
            GALLERY_LIST_URL,
            {"name": searched_name}
        )

        self.assertEqual(
            response.context["gallery_list"][0],
            Gallery.objects.get(name=searched_name)
        )

    def test_search_gallery_by_extra_long_name(self):
        searched_name = "a" * 256
        response = self.client.get(
            GALLERY_LIST_URL,
            {"name": searched_name}
        )

        self.assertEqual(
            list(response.context["gallery_list"]),
            list(Gallery.objects.all())
        )


class PublicGenreTest(TestCase):
    def test_login_required(self):
        response = self.client.get(GENRE_LIST_URL)

        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(
            response,
            f"/accounts/login/?next={GENRE_LIST_URL}"
        )


class PrivateGenreTest(TestCase):
    def setUp(self):
        for i in range(10):
            Genre.objects.create(
                name=f"test_{i}"
            )

        user = get_user_model().objects.create(
            username="riauser",
            password="r1@useR",
            pseudonym=f"ria"
        )
        self.client.force_login(user)

    def test_all_genres(self):
        paginated_by = 10
        response = self.client.get(GENRE_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["genre_list"]),
            list(Genre.objects.all())[:paginated_by]
        )

    def test_search_genre_by_name(self):
        searched_name = "test_9"
        response = self.client.get(
            GENRE_LIST_URL,
            {"name": searched_name}
        )

        self.assertEqual(
            response.context["genre_list"][0],
            Genre.objects.get(name=searched_name)
        )

    def test_search_genre_by_extra_long_name(self):
        searched_name = "a" * 256
        response = self.client.get(
            GENRE_LIST_URL,
            {"name": searched_name}
        )

        self.assertEqual(
            list(response.context["genre_list"]),
            list(Genre.objects.all())
        )
