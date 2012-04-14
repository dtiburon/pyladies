from django.views.generic import DetailView,ListView
from django.http import HttpResponseRedirect,HttpResponse
from pyladies.blog.models import Author,BlogPost
import json

class AuthorList(ListView):
    model = Author
    context_object_name = "author_list"
    template_name = "blog/author_list.html"

class AuthorDetail(DetailView):
    model = Author
    context_object_name = "author"
    template_name = "blog/author_detail.html"

class BlogPostList(ListView):
    model = BlogPost
    context_object_name = "blog_post_list"
    template_name = "blog/post_list.html"

class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "blog_post"
    template_name = "blog/post_detail.html"
