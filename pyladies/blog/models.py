from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from pyladies.utils.choices import PYLADIES_CHAPTERS,ROLES
from taggit.managers import TaggableManager


class Author(models.Model):
    name = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'))
    user = models.ForeignKey(User)
    role = models.CharField(_('role'),max_length=2,choices=ROLES,blank=True,null=True)
    chapter = models.CharField(_('chapter'),max_length=3,choices=PYLADIES_CHAPTERS)
    photo = models.ImageField(_('image field'),upload_to='/var/data/images/',blank=True,null=True)
    personal_homepage = models.URLField(_('personal homepage'),blank=True,null=True)
    twitter_username = models.URLField(_('twitter username'),blank=True,null=True)
    bio = models.TextField(_('biography'),blank=True,null=True)

    def __unicode__(self):
        return self.name

class BlogPostManager(models.Manager):
    def get_published(self):
        return self.filter(published=True)

class BlogPost(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'))
    author = models.ForeignKey(Author)
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
