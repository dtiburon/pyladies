from django.conf.urls.defaults import *
from pyladies.calendar.views import EventList,EventDetail

urlpatterns = patterns('',
    (r'(?P<slug>[-\w]+)', EventDetail.as_view()),
    (r'$', EventList.as_view()),
)
