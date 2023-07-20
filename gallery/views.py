from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin

from gallery.forms import (
    CustomUserCreationForm,
    UserSearchForm,
    GenreSearchForm,
    GallerySearchForm,
    ArtPieceUploadForm
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)

        pseudonym = self.request.GET.get("pseudonym", "")

        context["search_form"] = UserSearchForm(
            initial={
                "pseudonym": pseudonym
            }
        )

        return context

    def get_queryset(self):
        queryset = get_user_model().objects.all()

        form = UserSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                pseudonym__icontains=form.cleaned_data["pseudonym"]
            )

        return queryset


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()


class UserCreateView(LoginRequiredMixin, generic.CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("gallery:user-list")


class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("gallery:user-list")


class GenreListView(LoginRequiredMixin, generic.ListView):
    model = Genre
    context_object_name = "genre_list"
    template_name = "gallery/genre_list.html"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GenreListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = GenreSearchForm(
            initial={
                "name": name
            }
        )

        return context

    def get_queryset(self):
        queryset = Genre.objects.all()

        form = GenreSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return queryset


class GenreCreateView(LoginRequiredMixin, generic.CreateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("gallery:genre-list")


class GenreUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("gallery:genre-list")


class GenreDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("gallery:genre-list")


class GalleryListView(LoginRequiredMixin, generic.ListView):
    model = Gallery
    context_object_name = "gallery_list"
    template_name = "gallery/gallery_list.html"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GalleryListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = GallerySearchForm(
            initial={
                "name": name
            }
        )

        return context

    def get_queryset(self):
        queryset = Gallery.objects.all()

        form = GallerySearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return queryset


class GalleryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Gallery
    fields = "__all__"
    success_url = reverse_lazy("gallery:gallery-list")


class GalleryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Gallery
    fields = "__all__"
    success_url = reverse_lazy("gallery:gallery-list")


class GalleryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Gallery
    fields = "__all__"
    success_url = reverse_lazy("gallery:gallery-list")


class GalleryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Gallery


class ArtPieceListView(LoginRequiredMixin, generic.ListView):
    model = ArtPiece
    context_object_name = "art_piece_list"
    template_name = "gallery/art_piece_list.html"
    paginate_by = 6


class ArtPieceCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ArtPieceUploadForm()
        return render(request, 'gallery/art_piece_upload.html', {'form': form})

    def post(self, request):
        form = ArtPieceUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery:art-piece-list')
        else:
            return render(request, 'gallery/art_piece_upload.html', {'form': form})


class ArtPieceDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = ArtPiece
    fields = "__all__"
    context_object_name = "art_piece"
    template_name = "gallery/art_piece_confirm_delete.html"
    success_url = reverse_lazy("gallery:art-piece-list")


class ArtPieceDetailView(LoginRequiredMixin, generic.DetailView):
    model = ArtPiece
    context_object_name = "art_piece"
    template_name = "gallery/art_piece_detail.html"
