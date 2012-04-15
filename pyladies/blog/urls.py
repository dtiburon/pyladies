from django.conf.urls.defaults import *
from pyladies.blog.views import BlogPostList,BlogPostDetail,LatestEntriesFeed

urlpatterns = patterns('',
    (r'rss/$',LatestEntriesFeed()),
    (r'author/(?P<author_slug>[-\w]+)$', BlogPostList.as_view()),
    (r'(?P<pub_date__year>[0-9]+)/(?P<pub_date__month>[0-9]+)/(?P<pub_date__day>[0-9]+)/(?P<slug>[-\w]+)', BlogPostDetail.as_view()),
    (r'$', BlogPostList.as_view()),

)
