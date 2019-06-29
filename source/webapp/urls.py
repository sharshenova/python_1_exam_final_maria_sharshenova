from django.urls import path
from .views import UserDetailView, UserUpdateView, AuthorListView, AuthorDetailView, AuthorCreateView, \
    AuthorUpdateView, AuthorDeleteView, BookListView, BookDetailView, BookCreateView, BookUpdateView, \
    BookDeleteView, ReviewUpdateView, ReviewDeleteView, ReviewCreateView
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
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_details'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('book/<int:pk>/review/create/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/update', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete', ReviewDeleteView.as_view(), name='review_delete'),
]
