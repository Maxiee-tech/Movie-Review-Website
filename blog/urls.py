from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView

app_name = 'blog'

urlpatterns = [
    path('', BlogPostListView.as_view(), name='list'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='detail'),
    path('add/', BlogPostCreateView.as_view(), name='add'),
]