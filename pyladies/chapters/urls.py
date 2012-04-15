from django.conf.urls.defaults import *
from pyladies.chapters.views import MemberList,MemberDetail,ChapterList,ChapterDetail

urlpatterns = patterns('',
    (r'members/(?P<slug>[-\w]+)', MemberDetail.as_view()),
    (r'(?P<chapter_slug>[-\w]+)/members', MemberList.as_view()),
    (r'(?P<slug>[-\w]+)', ChapterDetail.as_view()),
    (r'$', ChapterList.as_view()),

)
