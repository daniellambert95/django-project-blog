from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.

class TestViews(TestCase):

    #  setUp method will be carried out before tests are have started
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testuser", password="password"
        )
    
    #  tearDown method will be carried out after tests are complete
    def tearDown(self):
        self.user.delete()

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertAlmostEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertAlmostEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/logout.html')

    def test_profile_view(self):
        self.client.login(username='testuser', password='password') 
        response = self.client.get(reverse('profile'))
        self.assertAlmostEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')
        
    def test_profile_redirect_view(self):
        response = self.client.get(reverse('profile'))
        redirect = self.client.get(reverse('login'))
        self.assertAlmostEquals(response.status_code, 302)
        self.assertTemplateUsed(redirect, 'users/login.html')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertAlmostEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
        
