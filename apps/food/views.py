from django.shortcuts import render
from django.views.generic import ListView

from .models import Food


class HomePageView(ListView):
    model = Food
    template_name = "index.html"
    queryset = Food.objects.filter(name__contains="berry").filter(color="red")

