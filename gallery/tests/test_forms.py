import datetime

from django.core.files.uploadedfile import SimpleUploadedFile

from django.test import TestCase

from gallery.forms import CustomUserCreationForm, ArtPieceUploadForm, ArtPieceUpdateForm


class CustomUserCreationFormTestCase(TestCase):

    def test_valid_data(self):
        form_data = {
            "username": "test_username",
            "password1": "1Qazxrw@",
            "password2": "1Qazxrw@",
            "pseudonym": "test_pseudonym",
            "first_name": "John",
            "last_name": "Doe",
            "is_author": True,
            "birth_date": None,
            "death_date": None,
            "country": None,
        }

        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class ArtPieceUploadFormTestCase(TestCase):
    def test_valid_data(self):
        picture = SimpleUploadedFile("filename.png",
                                     (b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
                                      b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
                                      b'\x02\x4c\x01\x00\x3b'
                                      ))
        image_data = {
            "picture": picture
        }
        form_data = {
            "title": "test_title",
            "picture": picture,
            "description": "test_description",
            "creation_date": datetime.date(2020, 4, 21),
            "author": None,
            "genre": None,
            "gallery": None,
        }

        form = ArtPieceUploadForm(data=form_data, files=image_data)
        print(form.errors)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class ArtPieceUpdateFormTestCase(TestCase):
    def test_valid_data(self):
        form_data = {
            "title": "title",
            "description": "test_description",
            "creation_date": datetime.date(2022, 4, 21),
            "author": None,
            "genre": None,
            "gallery": None,
        }

        form = ArtPieceUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
