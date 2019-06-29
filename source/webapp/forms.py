from django import forms
from django.contrib.auth.models import User
from .models import Author


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
        fields = ['name', 'birth_date', 'death_date', 'bio']