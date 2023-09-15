from django.shortcuts import render, get_object_or_404, redirect
from news.models.news_model import News
from news.forms import CategoryForm, NewsForm

# Create your views here.


def index(request):
    news = News.objects.all()

    return render(request, "home.html", {"news": news})


def news_details(request, news_id):
    news = get_object_or_404(News, id=news_id)
    context = {"news": news, "categories": news.categories.all()}

    return render(request, "news_details.html", context)


def create_category(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")

    return render(request, "categories_form.html", {"form": form})


def create_news(request):
    form = NewsForm()

    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("home-page")

    return render(request, "news_form.html", {"form": form})
