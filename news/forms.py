from django import forms
from news.models.category_model import Categories


class CategoryForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Categories

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "Nome"
