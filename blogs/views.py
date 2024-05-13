from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView

from blogs.models import Blog


# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', )
    success_url = reverse_lazy('main:index')
