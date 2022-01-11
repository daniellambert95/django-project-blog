from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name = 'home-page'),
    path('blog/', views.blog, name = 'blog-home'),
    path('about/', views.about, name = 'about-page'),
    
]

