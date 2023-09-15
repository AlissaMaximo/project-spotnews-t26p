from django.shortcuts import render, get_object_or_404, redirect
from news.models.news_model import News
from news.forms import CategoryForm

# Create your views here.


def index(request):
    news = News.objects.all()
    context = {"news": news}

    return render(request, "home.html", context)


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
    else:
        form = CategoryForm()
    context = {"form": form}

    return render(request, "categories_form.html", context)
