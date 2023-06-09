from apps.articles.views import ArticleDetailView, ArticleListView
from django.urls import path

urlpatterns = [
    path("<slug:slug>", ArticleDetailView.as_view(), name="article_detail"),
    path("", ArticleListView.as_view(), name="article_list"),
]
