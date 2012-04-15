from django.conf.urls.defaults import *
from pyladies.blog.views import BlogPostList,BlogPostDetail

urlpatterns = patterns('',
    (r'author/(?P<author_slug>[-\w]+)$', BlogPostList.as_view()),
    (r'(?P<slug>[-\w]+)', BlogPostDetail.as_view()),
    (r'$', BlogPostList.as_view()),

)
