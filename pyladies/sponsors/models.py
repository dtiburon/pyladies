from django.db import models
from django.utils.translation import ugettext_lazy as _
from pyladies.utils.choices import PYLADIES_CHAPTERS
from taggit.managers import TaggableManager

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
