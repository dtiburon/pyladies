from django.db import models
from django.utils.translation import ugettext_lazy as _


class HomePage(models.Model):
    title = models.CharField(_('title'), max_length=200)
    mission_statement = models.TextField(_('mission statement'))
    content = models.TextField(_('content'))

    def __unicode__(self):
        return "Home Page: %s" % (self.title)
