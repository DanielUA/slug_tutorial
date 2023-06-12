from django.urls import path

from apps.rss.models import Tutorial
from apps.rss.views import TutorialDetailView, TutorialListView

urlpatterns = [
    path("<slug:slug>", TutorialDetailView.as_view(), name="tutorial_detail"),
    path("", TutorialListView.as_view(), name="tutorial_list"),

]
