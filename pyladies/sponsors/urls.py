from django.conf.urls.defaults import *
from pyladies.sponsors.views import SponsorList,SponsorDetail

urlpatterns = patterns('',
    (r'(?P<slug>[-\w]+)', SponsorDetail.as_view()),
    (r'$', SponsorList.as_view()),

)
