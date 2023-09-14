from django.shortcuts import render
from news.models.news_model import News

# Create your views here.


def index(request):
    news = News.objects.all()
    context = {"news": news}

    return render(request, "home.html", context)
