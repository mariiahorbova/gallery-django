import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from gallery.models import ArtPiece, Genre, Gallery


class AdminSiteTestMixin(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="riadmin",
            password="ri@dm1n"
        )
        self.client.force_login(self.admin_user)


class UserAdminSiteTest(AdminSiteTestMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.user = get_user_model().objects.create_superuser(
            username="testuser",
            password="te$suse&",
            first_name="TestUserFirst",
            last_name="TestUserLast",
            pseudonym="TestPseudo",
            is_author=True
        )

    def test_user_pseudonym_change(self):
        url = reverse("admin:gallery_user_change", args=[self.user.id])
        response = self.client.get(url)

        self.assertContains(response, self.user.pseudonym)

    def test_user_add(self):
        url = reverse("admin:gallery_user_add")
        response = self.client.get(url)
        self.assertContains(response, "First name")
        self.assertContains(response, "Last name")
        self.assertContains(response, "Pseudonym")

    def test_search_user(self):
        url = reverse(
            "admin:gallery_user_changelist",
        ) + "?username=testuser"
        response = self.client.get(url)

        self.assertContains(response, "testuser")


class ArtPieceAdminSiteTest(AdminSiteTestMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.art_piece = ArtPiece(
            title="Sunflower",
            picture="pictures/icon.png",
            description="test_desc",
            creation_date=datetime.date(2020, 4, 21)
        )
        self.art_piece.save()

    def test_title_change(self):
        url = reverse("admin:gallery_artpiece_change", args=[self.art_piece.id])
        response = self.client.get(url)

        self.assertContains(response, self.art_piece.title)

    def test_art_piece_add(self):
        url = reverse("admin:gallery_artpiece_add")
        response = self.client.get(url)
        self.assertContains(response, "Title")
        self.assertContains(response, "Description")
        self.assertContains(response, "Picture")


class GenreAdminSiteTest(AdminSiteTestMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.genre = Genre.objects.create(
            name="test_genre"
        )

    def test_search_genre(self):
        url = reverse(
            "admin:gallery_genre_changelist",
        ) + "?name=Renaissance"
        response = self.client.get(url)

        self.assertNotContains(response, "test_genre")


class GalleryAdminSiteTest(AdminSiteTestMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.gallery = Gallery.objects.create(
            name="Lehman Maupin"
        )

    def test_search_gallery(self):
        url = reverse(
            "admin:gallery_gallery_changelist",
        ) + "?name=Lehman+Maupin"
        response = self.client.get(url)

        self.assertContains(response, "Lehman Maupin")
