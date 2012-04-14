from django.contrib import admin
from pyladies.calendar.models import Event

class EventOptions(admin.ModelAdmin):
    list_display = ('title','chapter','start_date','active')
    list_filter = ['chapter','active','start_date','event_type']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Event, EventOptions)
