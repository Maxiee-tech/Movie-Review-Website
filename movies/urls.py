from django.urls import path
from .views import MovieListView, MovieDetailView, MovieCreateView

app_name = 'movies'

urlpatterns = [
    path('', MovieListView.as_view(), name='list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='detail'),
    path('add/', MovieCreateView.as_view(), name='add'),
]