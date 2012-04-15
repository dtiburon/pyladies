from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from pyladies.chapters.models import Member
from taggit.managers import TaggableManager



class BlogPostManager(models.Manager):
    def get_published(self):
        return self.filter(published=True).order_by('-pub_date')

class BlogPost(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'))
    author = models.ForeignKey(Member)
    content = models.TextField(_('content'))
    published = models.BooleanField(_('published'),default=False)
    pub_date = models.DateTimeField(_('publish date'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    tags = TaggableManager()

    objects = BlogPostManager()

    class Meta:
        ordering = ['-updated',]

    def __unicode__(self):
        return "Blog: %s" % (self.title)

    def get_absolute_url(self):
        return "/blog/%s/%s/%s/%s" % (self.pub_date.year,self.pub_date.month,self.pub_date.day,\
            self.slug)
