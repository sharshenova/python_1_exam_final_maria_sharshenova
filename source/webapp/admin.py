from django.contrib import admin
from webapp.models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'birth_date', 'death_date', 'bio']

admin.site.register(Author, AuthorAdmin)
