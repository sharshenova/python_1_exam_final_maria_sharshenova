from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from webapp.forms import UserForm, AuthorForm, BookForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from webapp.models import Author, Book
from django.urls import reverse_lazy


class UserDetailView(DetailView):
    template_name = 'user_details.html'
    model = User


class UserUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = User
    template_name = 'user_update.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('webapp:user_details', kwargs={'pk': self.object.pk})

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if user != self.request.user:
            return HttpResponseRedirect(reverse('webapp:user_details', kwargs={'pk': pk}))
        return super().get(request, pk=pk)

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user == self.get_object().author


class AuthorDetailView(DetailView):
    template_name = 'author_details.html'
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['books_by_author'] = self.object.books.all()
        return context


class AuthorListView(ListView):
    template_name = 'author_list.html'
    model = Author
    queryset = Author.objects.filter(is_deleted=False)


class AuthorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'author_create.html'
    form_class = AuthorForm
    model = Author

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user.is_staff


class AuthorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'author_update.html'
    form_class = AuthorForm
    model = Author

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user.is_staff


class AuthorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'author_delete.html'
    model = Author
    success_url = reverse_lazy('webapp:author_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()
        return HttpResponseRedirect(self.get_success_url())

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user.is_staff


class BookDetailView(DetailView):
    template_name = 'book_details.html'
    model = Book


class BookListView(ListView):
    template_name = 'book_list.html'
    model = Book


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'book_create.html'
    form_class = BookForm
    model = Book

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user.is_staff


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'book_update.html'
    form_class = BookForm
    model = Book

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user.is_staff


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'book_delete.html'
    model = Book
    success_url = reverse_lazy('webapp:book_list')

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user.is_staff