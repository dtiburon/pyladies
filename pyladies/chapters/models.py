from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from pyladies.utils.choices import ROLES
from taggit.managers import TaggableManager

class ChapterManager(models.Manager):
    def get_active(self):
        return self.filter(active=True)



class Chapter(models.Model):
    name = models.CharField(_('name'), max_length=200)
    slug = models.SlugField(_('slug'))
    active = models.BooleanField(_('active'),default=True)
    chapter_homepage = models.URLField(_('chapter homepage'),blank=True,null=True)
    twitter_username = models.URLField(_('twitter username'),blank=True,null=True)
    description = models.TextField(_('description'),blank=True,null=True)
    location = models.CharField(_('location'),max_length=300)
    gmap_location = models.CharField(_('google map location'),max_length=250,blank=True,null=True)

    objects = ChapterManager()

    def __unicode__(self):
        return "Chapter: %s" % self.name

class MemberManager(models.Manager):
    def get_active(self):
        return self.filter(active=True)

class Member(models.Model):
    name = models.CharField(_('name'), max_length=200)
    slug = models.SlugField(_('slug'))
    user = models.ForeignKey(User)
    role = models.CharField(_('role'),max_length=2,choices=ROLES,blank=True,null=True)
    chapter = models.ForeignKey(Chapter)
    photo = models.ImageField(_('image field'),upload_to='/var/data/images/',blank=True,null=True)
    active = models.BooleanField(_('active'),default=True)
    personal_homepage = models.URLField(_('personal homepage'),blank=True,null=True)
    twitter_username = models.URLField(_('twitter username'),blank=True,null=True)
    bio = models.TextField(_('biography'),blank=True,null=True)


    objects = MemberManager()


    def __unicode__(self):
        return self.name
