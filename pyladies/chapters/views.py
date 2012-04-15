from django.views.generic import DetailView,ListView
from django.http import HttpResponseRedirect,HttpResponse
from pyladies.chapters.models import Member,Chapter
import json

class ChapterList(ListView):
    model = Chapter
    context_object_name = "chapter_list"
    template_name = "chapters/chapter_list.html"

    def get_queryset(self):
        chapter_slug = self.get('chapter_slug')
        if chapter_slug:
            try:
                chapter = Chapter.objects.get(slug = chapter_slug)
                return Chapter.objects.get_active().filter(chapter=chapter)
            except Chapter.DoesNotExist:
                pass
        return Chapter.objects.get_active()

class ChapterDetail(DetailView):
    model = Chapter
    context_object_name = "chapter"
    template_name = "chapters/chapter_detail.html"

class MemberList(ListView):
    model = Member
    context_object_name = "member_list"
    template_name = "chapters/member_list.html"

class MemberDetail(DetailView):
    model = Member
    context_object_name = "member"
    template_name = "chapters/member_detail.html"
