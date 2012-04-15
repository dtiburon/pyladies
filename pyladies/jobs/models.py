from django.db import models
from django.utils.translation import ugettext_lazy as _
from pyladies.utils.choices import PYLADIES_CHAPTERS
from taggit.managers import TaggableManager


JOB_TYPE = (
    ('FT','Full Time'),
    ('PT','Part Time'),
    ('CO','Contract'),
)


SPONSOR_LEVEL = (
    ('GO','Gold'),
    ('SI','Silver'),
    ('BZ','Bronze'),
    ('SP','Supporters'),
    ('BZ','Friends'),
)

class SponsorManager(models.Manager):
    def get_active(self):
        return self.filter(active=True)


class Sponsor(models.Model):
    name = models.CharField(_('name'),max_length=250)
    slug = models.SlugField(_('slug'))
    level = models.CharField(_('level'),max_length=2,choices=SPONSOR_LEVEL)
    company_website = models.URLField(_('company website'),blank=True,null=True)
    logo = models.ImageField(_('image field'),upload_to='/var/data/images/',blank=True,null=True)
    photo = models.ImageField(_('image field'),upload_to='/var/data/images/',blank=True,null=True)
    active = models.BooleanField(_('active'),default=True)
    location = models.CharField(_('location'),max_length=300)
    gmap_location = models.CharField(_('google map location'),max_length=250,blank=True,null=True)
    description = models.TextField(_('description'),blank=True,null=True)
    
    objects = SponsorManager()
    

    def __unicode__(self):
        return "Sponsor: %s" % self.name



class JobManager(models.Manager):
    def get_active(self):
        return self.filter(active=True)


class Job(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'))
    company_name = models.CharField(_('company name'),max_length=200)
    company_slug = models.SlugField(_('company slug'))
    job_type = models.CharField(_('job type'),max_length=2,choices=JOB_TYPE)
    description = models.TextField(_('description'), blank=True)
    related_sponsor = models.ForeignKey(Sponsor,blank=True,null=True)
    active = models.BooleanField(_('active'),default=True)
    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'),blank=True,null=True)
    location = models.CharField(_('location'),max_length=300)
    gmap_location = models.CharField(_('google map location'),max_length=250,blank=True,null=True)
    application_website = models.URLField(_('application website'),blank=True,null=True)
    company_website = models.URLField(_('company website'),blank=True,null=True)


    objects = JobManager()

    class Meta:
        ordering = ('-start_date','title')

    def __unicode__(self):
        return "Job: %s" % (self.title)


