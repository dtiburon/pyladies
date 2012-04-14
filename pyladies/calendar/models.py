from django.db import models
from django.utils.translation import ugettext_lazy as _
from pyladies.utils.choices import PYLADIES_CHAPTERS
from taggit.managers import TaggableManager


EVENT_TYPE = (
    ('HA','Hackathon'),
    ('WK','Workshop'),
    ('SO','Social Event'),

)


class EventManager(models.Manager):
    def get_active(self):
        return self.filter(active=True)


class Event(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'))
    event_type = models.CharField(_('event type'),max_length=2,choices=EVENT_TYPE)
    chapter = models.CharField(_('chapter'),max_length=3,choices=PYLADIES_CHAPTERS)
    description = models.TextField(_('description'), blank=True)
    active = models.BooleanField(_('active'),default=True)
    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'),blank=True,null=True)
    start_time = models.TimeField(_('start time'))
    end_time = models.TimeField(_('end time'))
    location = models.CharField(_('location'),max_length=300)
    gmap_location = models.CharField(_('google map location'),max_length=250,blank=True,null=True)


    objects = EventManager()

    class Meta:
        ordering = ('-start_date','title')

    def __unicode__(self):
        return "Event: %s" % (self.title)


