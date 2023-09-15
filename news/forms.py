from django import forms
from news.models.category_model import Categories
from news.models.news_model import News
from news.models.user_model import Users


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label="Nome", max_length=200)

    class Meta:
        model = Categories
        fields = ["name"]


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            "title",
            "content",
            "author",
            "created_at",
            "image",
            "categories",
        ]

    title = forms.CharField(label="Título", max_length=200)
    content = forms.CharField(
        label="Conteúdo",
        widget=forms.Textarea(attrs={"type": "textarea"}),
        max_length=200,
    )
    author = forms.ModelChoiceField(
        label="Autoria", queryset=Users.objects.all()
    )
    created_at = forms.DateField(
        label="Criado em", widget=forms.DateTimeInput(attrs={"type": "date"})
    )
    image = forms.FileField(label="URL da Imagem", required=False)
    categories = forms.ModelMultipleChoiceField(
        label="Categorias",
        widget=forms.CheckboxSelectMultiple,
        queryset=Categories.objects.all(),
    )
