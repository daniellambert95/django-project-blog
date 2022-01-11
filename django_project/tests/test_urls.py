from django.test import TestCase
from django.urls import reverse, resolve

# Create your tests here.

class TestMainUrls(TestCase):

    def test_home_page_url(self):
        url = reverse('home-page')
        resolver = resolve('/')
        self.assertEqual(url, '/')
        self.assertEqual(resolver.view_name, 'home-page')

    def test_register_url(self):
        url = reverse('register')
        resolver = resolve('/register/')
        self.assertEqual(url, '/register/')
        self.assertEqual(resolver.view_name, 'register')

    def test_profile_url(self):
        url = reverse('profile')
        resolver = resolve('/profile/')
        self.assertEqual(url, '/profile/')
        self.assertEqual(resolver.view_name, 'profile')

    def test_login_url(self):
        url = reverse('login')
        resolver = resolve('/login/')
        self.assertEqual(url, '/login/')
        self.assertEqual(resolver.view_name, 'login')

    def test_logout_url(self):
        url = reverse('logout')
        resolver = resolve('/logout/')
        self.assertEqual(url, '/logout/')
        self.assertEqual(resolver.view_name, 'logout')

    def test_about_page_url(self):
        url = reverse('about-page')
        resolver = resolve('/about/')
        self.assertEqual(url, '/about/')
        self.assertEqual(resolver.view_name, 'about-page')


class TestBlogUrls(TestCase):
    def test_blog_url(self):
        url = reverse('blog-home')
        resolver = resolve('/blog/')
        self.assertEqual(url, '/blog/')
        self.assertEqual(resolver.view_name, 'blog-home')
    
