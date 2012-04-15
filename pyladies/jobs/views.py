from django.views.generic import DetailView,ListView
from django.http import HttpResponseRedirect,HttpResponse
from pyladies.jobs.models import Job,Sponsor
import json

class JobList(ListView):
    model = Job
    context_object_name = "job_list"
    template_name = "jobs/job_list.html"

class JobDetail(DetailView):
    model = Job
    context_object_name = "job"
    template_name = "jobs/job_detail.html"

class SponsorList(ListView):
    model = Sponsor
    context_object_name = "sponsor_list"
    template_name = "jobs/sponsor_list.html"

class SponsorDetail(DetailView):
    model = Sponsor
    context_object_name = "sponsor"
    template_name = "jobs/sponsor_detail.html"
