from django.contrib import admin
from webapp.models import Author, Book, Review


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'birth_date', 'death_date', 'bio', 'is_deleted']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['pk', 'text', 'author', 'book', 'created_at']


class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'author', 'published_at', 'file', 'image', 'description']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)