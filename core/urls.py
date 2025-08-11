from django.urls import path
from .views import HomeView, TrendingView, SearchView, analytics_view, TopRatedView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('trending/', TrendingView.as_view(), name='trending'),
    path('search/', SearchView.as_view(), name='search'),
    path('analytics/', analytics_view, name='analytics'),
    path('top-rated/', TopRatedView.as_view(), name='top_rated'),
]