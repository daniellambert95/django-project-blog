from django.urls import path
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    LikeView,
    LoveView,
    UserPostListView,
    
)
from . import views


urlpatterns = [
    
    path('blog/', PostListView.as_view(), name = 'blog-home'),
    path('blog/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('blog/new/', PostCreateView.as_view(), name = 'post-create'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('like/<int:pk>/', LikeView, name = 'like-post'),
    path('love/<int:pk>/', LoveView, name = 'love-post'),
    
]

