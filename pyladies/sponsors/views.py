from django.views.generic import DetailView,ListView
from django.http import HttpResponseRedirect,HttpResponse
from pyladies.sponsors.models import Sponsor
import json


class SponsorList(ListView):
    model = Sponsor
    context_object_name = "sponsor_list"
    template_name = "jobs/sponsor_list.html"

class SponsorDetail(DetailView):
    model = Sponsor
    context_object_name = "sponsor"
    template_name = "jobs/sponsor_detail.html"
