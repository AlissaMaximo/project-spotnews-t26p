from django import forms


class CategoryForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        label="Nome",
    )
