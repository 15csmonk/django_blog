from django.contrib.syndication.views import Feed

from .models import Post

class AllPostRssFeed(Feed):
    title = "Just for fun！"

    link = "/"
    description = "myblog"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[{}] {}'.format(item.category, item.title)

    def item_description(self, item):
        return item.content