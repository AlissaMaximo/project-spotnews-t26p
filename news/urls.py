from django.urls import path
from news.views import index, news_details, create_category, create_news

urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:news_id>", news_details, name="news-details-page"),
    path("categories/", create_category, name="categories-form"),
    path("news/", create_news, name="news-form"),
]
