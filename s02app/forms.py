import datetime

from django import forms

from .models import Author, Article


class RandomForm(forms.Form):
    EVENT_CHOICES = [
        ('coin', 'Монетка'),
        ('dice', 'Кубик'),
        ('number', 'Числа')
    ]

    event_type = forms.ChoiceField(choices=EVENT_CHOICES, label='Выберите игру')
    attempts = forms.IntegerField(min_value=1, max_value=64, label='Количество попыток')


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea)
    birthday = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))


class ArticleForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    # author = forms.ModelChoiceField(queryset=Author.objects.all())
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    category = forms.CharField()
    is_published = forms.BooleanField(initial=False)
