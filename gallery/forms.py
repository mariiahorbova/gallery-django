from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from gallery.models import ArtPiece


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            "pseudonym",
            "first_name",
            "last_name",
            "birth_date",
            "death_date",
            "country",
            "is_author"
        )
        widgets = {
            "birth_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date"
                }),
            "death_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date"
                }),
        }


class GenreSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by genre.."
            }
        )
    )


class UserSearchForm(forms.Form):
    pseudonym = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username.."
            }
        )
    )


class GallerySearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name.."
            }
        )
    )


class ArtPieceUploadForm(forms.ModelForm):

    class Meta:
        model = ArtPiece
        fields = [
            "title",
            "picture",
            "description",
            "creation_date",
            "author",
            "genre",
            "gallery"
        ]
        widgets = {
            "creation_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date"
                }),
        }


class ArtPieceUpdateForm(ArtPieceUploadForm):

    class Meta(ArtPieceUploadForm.Meta):
        exclude = ["picture"]
