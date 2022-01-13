from django.shortcuts import render
from .models import Post
import logging

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

logger = logging.getLogger("my_logger")

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    
    logger.info("A user has visited the sites blog page.")
    return render(request, 'blog/blog_home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

