from django.conf.urls.defaults import *
from pyladies.homepage.views import home_page


urlpatterns = patterns('',
    (r'$',home_page),
)

