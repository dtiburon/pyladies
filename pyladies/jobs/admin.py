from django.contrib import admin
from pyladies.jobs.models import Job,Sponsor

class JobOptions(admin.ModelAdmin):
    list_display = ('title','company_name','start_date','active')
    list_filter = ['job_type','start_date','active']
    prepopulated_fields = {"slug": ("title",),"company_slug": ("company_name",)}


class SponsorOptions(admin.ModelAdmin):
    list_display = ('name','level','active',)
    list_filter = ['level','active',]
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Job, JobOptions)
admin.site.register(Sponsor, SponsorOptions)
