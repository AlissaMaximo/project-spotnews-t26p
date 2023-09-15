from django import forms
from news.models.category_model import Categories


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nome")

    class Meta:
        model = Categories
        fields = ["name"]
