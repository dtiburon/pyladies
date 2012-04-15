from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from pyladies.blog.models import BlogPost
from pyladies.chapters.models import Member,Chapter
from pyladies.calendar.models import Event
from pyladies.homepage.models import HomePage

import json

def home_page(request):
    chapters = Chapter.objects.get_active()
    members = Member.objects.get_active()
    blog_posts = BlogPost.objects.get_published()
    events = Event.objects.get_active()
    home_page_details = HomePage.objects.all()[0]

    context = {
        'chapters': chapters,
        'members':members,
        'blog_posts':blog_posts,
        'events':events,
        'home_page_details':home_page_details,
    }
    return render_to_response('index.html',context,context_instance=RequestContext(request))


