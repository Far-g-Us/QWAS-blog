from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'article']


class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Выберите дату рождения',
    )
    class Meta:
        model = CustomUser
        fields = ['full_name', 'birth_date', 'username', 'password1', 'password2']