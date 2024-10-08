from django import forms
from django.forms import widgets

from webapp.models import Post


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти",
                             widget=widgets.Input(attrs={'class': 'form-control me-2'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content", "image"]
