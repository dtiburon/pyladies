from django.contrib import admin
from pyladies.chapters.models import Chapter,Member

class ChapterOptions(admin.ModelAdmin):
    list_display = ('name','active','location')
    list_filter = ['active',]
    prepopulated_fields = {"slug": ("name",)}


class MemberOptions(admin.ModelAdmin):
    list_display = ('name','chapter',)
    list_filter = ['chapter','active']
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Chapter, ChapterOptions)
admin.site.register(Member, MemberOptions)
