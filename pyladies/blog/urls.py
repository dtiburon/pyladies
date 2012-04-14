from django.conf.urls.defaults import *
from pyladies.blog.views import AuthorList,AuthorDetail,BlogPostList,BlogPostDetail

urlpatterns = patterns('',
    (r'authors/(?P<slug>[-\w]+)', AuthorDetail.as_view()),
    (r'authors$', AuthorList.as_view()),
    (r'(?P<slug>[-\w]+)', BlogPostDetail.as_view()),
    (r'$', BlogPostList.as_view()),

)
