from django import forms
from django.contrib.auth.models import User
from .models import Author, Book, Review


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class AuthorForm(forms.ModelForm):
    def clean(self):
        if not self.cleaned_data['name']:
            raise forms.ValidationError('Поле "ФИО" должно быть заполнено')
        return super().clean()

    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'death_date', 'bio', 'image']


class BookForm(forms.ModelForm):
    def clean(self):
        if not self.cleaned_data['title'] or not self.cleaned_data['author'] or not self.cleaned_data['published_at']:
            raise forms.ValidationError('Поля "название", "автор" и "год издания" должны быть заполнены')
        return super().clean()

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_at', 'file', 'image', 'description']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']