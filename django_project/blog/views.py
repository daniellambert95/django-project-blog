from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)

import logging

logger = logging.getLogger("django")

def home(request):

    logger.info("A user has visited the sites home page.")
    logger.debug(request)
    return render(request, 'blog/home.html')


def about(request):

    logger.info("A user has visited the sites about page.")
    logger.debug(request)
    return render(request, 'blog/about.html', {'title': 'About'})


def blog(request, **kwargs):
    context = {
        'posts': Post.objects.all(),
    }
    
    post_id = get_object_or_404(Post, id = kwargs['pk'])
    total_likes = post_id.total_likes()
    context['total_likes'] = total_likes

    logger.info("A user has visited the sites blog page.")
    logger.debug(request)
    return render(request, 'blog/blog_home.html', context)

def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog-home'))



class PostListView(ListView):
    model = Post
    template_name = "blog/blog_home.html"
    context_object_name = "posts"
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreatelView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']


    #  Here we are returning a function at overrides the inherited class's
    #  form_valid and assigning the signed in user as the author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']


    #  Here we are returning a function at overrides the inherited class's
    #  form_valid and assigning the signed in user as the author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    #  This function will stop a user from updating a post if it's not their post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/blog/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False