from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Tutorial(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    is_live = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tutorial_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-update_at"]
