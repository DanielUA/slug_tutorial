from django.urls import path

from apps.posts.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home")
]
