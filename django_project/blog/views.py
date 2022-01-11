from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog_home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

