from django.views.generic import DetailView,ListView
from django.http import HttpResponseRedirect,HttpResponse
from pyladies.blog.models import BlogPost
from pyladies.chapters.models import Member
from django.contrib.syndication.views import Feed
import json

class BlogPostList(ListView):
    model = BlogPost
    context_object_name = "blog_post_list"
    template_name = "blog/post_list.html"

    def get_queryset(self):
        author_slug = self.get('author_slug')
        if author_slug:
            try:
                member = Member.objects.get(slug = author_slug)
                return BlogPost.objects.get_active().filter(member=member)
            except Member.DoesNotExist:
                pass
        return BlogPost.objects.get_active()


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "blog_post"
    template_name = "blog/post_detail.html"


class LatestEntriesFeed(Feed):
    title = "PyLadies News"
    link = "/rss/"
    description = "Updates on PyLadies"

    def items(self):
        return BlogPost.objects.get_published()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
    
    
