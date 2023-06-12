from django.contrib import admin
from django.urls import path, include

from apps.rss.django_project.feeds import RssTutorialFeeds

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tutorials/", include("tutorials.urls")),
    path('feed/rss', RssTutorialFeeds(), name="tutorial_feed"),
]
