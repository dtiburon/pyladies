from django.contrib import admin
from pyladies.sponsors.models import Sponsor


class SponsorOptions(admin.ModelAdmin):
    list_display = ('name','level','active',)
    list_filter = ['level','active',]
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Sponsor, SponsorOptions)
