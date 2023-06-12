from django.views.generic import ListView, DetailView

from apps.rss.models import Tutorial


class TutorialListView(ListView):
    model = Tutorial
    context_object_name = "tutorial_list"
    template_name = "tutorial_list.html"


class TutorialDetailView(DetailView):
    model = Tutorial
    context_object_name = "tutorial"
    template_name = "tutorial_detail.html"
