from django.views.generic import DetailView,ListView
from django.http import HttpResponseRedirect,HttpResponse
from pyladies.calendar.models import Event
import json

class EventList(ListView):
    model = Event
    context_object_name = "event_list"
    template_name = "calendar/event_list.html"

class EventDetail(DetailView):
    model = Event
    context_object_name = "event"
    template_name = "calendar/event_detail.html"
