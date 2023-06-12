from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from apps.rss.models import Tutorial


class RssTutorialFeeds(Feed):
    title = "Tutorial"
    link = "/latesttutorial/"
    description = "Recent free totorials on LearnDjango.com"

    def items(self):
        return Tutorial.objects.all("-updated_at"[:100])

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)

    def item_lastupdated(self, item):
        return item.updated_at
