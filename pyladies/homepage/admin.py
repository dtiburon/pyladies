from django.contrib import admin
from pyladies.homepage.models import HomePage

class HomePageOptions(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(HomePage, HomePageOptions)
