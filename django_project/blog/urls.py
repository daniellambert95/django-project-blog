from django.urls import path
from .views import (
    PostListView, 
    PostDetailView,
    PostCreatelView,
    PostUpdateView,
    PostDeleteView,
    LikeView,
    LoveView,
    
)
from . import views


urlpatterns = [
    
    path('blog/', PostListView.as_view(), name = 'blog-home'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('blog/new/', PostCreatelView.as_view(), name = 'post-create'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('like/<int:pk>/', LikeView, name = 'like-post'),
    path('love/<int:pk>/', LoveView, name = 'love-post'),
    
]

