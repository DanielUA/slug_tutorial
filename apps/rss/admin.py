from django.contrib import admin

from apps.rss.models import Tutorial


class RssAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "description", "content"]
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(Tutorial, RssAdmin)
