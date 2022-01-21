from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from users.forms import ContactForm
from .models import Post
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.models import User
# from django.http import StreamingHttpResponse
# import os
# from WSGIREF.UTIL import FileWrapper
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

def contact_view(request):
    
    contact_form = ContactForm
    if request.method == 'POST':
        form = ContactForm(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name')
            contact_email = request.POST.get('contact_email')
            content = request.POST.get('content')

            template = get_template('blog/contact_form.txt')

            context = {
                'name' : name,
                'contact_email' : contact_email,
                'content' : content
            }
            
            context = template.render(context)
        

        email = EmailMessage(
            "New contact form email",
            context,
            "Daniels Django Project",
            ['danjlambert95@gmail.com'],
            headers = {'Reply to': contact_email}
        )

        email.send()
        messages.success(request, f'Your message has successfully been sent!')
        return redirect('home-page')

    return render(request, 'blog/contact.html', {'form':contact_form} )

def blog(request):
    context = {
        'posts': Post.objects.all(),
    }

    logger.info("A user has visited the sites blog page.")
    logger.debug(request)
    return render(request, 'blog/blog_home.html', context)

def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))

    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
#  This returns the same/page link that we're on
    return redirect(request.META['HTTP_REFERER'])

def LoveView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))

    if post.loves.filter(id = request.user.id).exists():
        post.loves.remove(request.user)
        liked = False
    else:
        post.loves.add(request.user)
        liked = True
    #  This returns the same/page link that we're on
    return redirect(request.META['HTTP_REFERER'])

class PostListView(ListView):
    model = Post
    template_name = "blog/blog_home.html"
    context_object_name = "posts"
    #  If I want to have the posts in order newest to oldest, add a '-' before date_posted
    ordering = ['date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    #  If I want to have the posts in order newest to oldest, add a '-' before date_posted
    # ordering = ['date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
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
    