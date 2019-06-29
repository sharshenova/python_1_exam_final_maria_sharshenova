from django.contrib import admin
from webapp.models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'birth_date', 'death_date', 'bio', 'is_deleted']


class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'author', 'published_at', 'file', 'image', 'description']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
