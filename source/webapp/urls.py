from django.urls import path
from .views import UserDetailView, UserUpdateView, AuthorListView, AuthorDetailView, AuthorCreateView, \
    AuthorUpdateView, AuthorDeleteView, BookListView, BookDetailView

app_name = 'webapp'

urlpatterns = [
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_details'),
    path('user/<int:pk>/update', UserUpdateView.as_view(), name='user_update'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_details'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
    path('', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_details')
]
