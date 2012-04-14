from django.contrib import admin
from pyladies.blog.models import BlogPost,Author

class BlogPostOptions(admin.ModelAdmin):
    list_display = ('title','pub_date','author','published')
    list_filter = ['author','updated','published']
    prepopulated_fields = {"slug": ("title",)}


class AuthorOptions(admin.ModelAdmin):
    list_display = ('name','chapter',)
    list_filter = ['chapter',]
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Author, AuthorOptions)
admin.site.register(BlogPost, BlogPostOptions)
