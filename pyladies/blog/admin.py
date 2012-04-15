from django.contrib import admin
from pyladies.blog.models import BlogPost

class BlogPostOptions(admin.ModelAdmin):
    list_display = ('title','pub_date','author','published')
    list_filter = ['author','updated','published']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(BlogPost, BlogPostOptions)
