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
        fields = "__all__"
        model = News

    author = forms.ModelChoiceField(
        label="Autoria", queryset=Users.objects.all()
    )
    title = forms.CharField(label="Título")
    categories = forms.ModelMultipleChoiceField(
        label="Categorias",
        widget=forms.CheckboxSelectMultiple,
        queryset=Categories.objects.all(),
    )
    content = forms.CharField(
        label="Conteúdo",
        widget=forms.Textarea(attrs={"type": "textarea"}),
    )
    created_at = forms.DateField(
        label="Criado em", widget=forms.DateTimeInput(attrs={"type": "date"})
    )
    image = forms.FileField(label="URL da Imagem", required=False)
