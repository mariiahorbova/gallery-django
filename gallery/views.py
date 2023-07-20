from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from gallery.forms import (
    CustomUserCreationForm,
)
from gallery.models import ArtPiece, Genre, Gallery


@login_required
def index(request):
    """View function for the home page of the site."""

    num_authors = get_user_model().objects.count()
    num_art_pieces = ArtPiece.objects.count()
    num_genres = Genre.objects.count()
    num_galleries = Gallery.objects.count()

    context = {
        "num_authors": num_authors,
        "num_art_pieces": num_art_pieces,
        "num_genres": num_genres,
        "num_galleries": num_galleries
    }

    return render(request, "index.html", context=context)


class UserListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    context_object_name = "user_list"
    template_name = "gallery/user_list.html"
    paginate_by = 10


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()


class UserCreateView(LoginRequiredMixin, generic.CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("gallery:user-list")


class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("gallery:user-list")
