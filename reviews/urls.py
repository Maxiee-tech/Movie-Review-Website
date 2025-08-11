from django.urls import path
from .views import ReviewListView, ReviewDetailView, ReviewCreateView

app_name = 'reviews'

urlpatterns = [
    path('', ReviewListView.as_view(), name='list'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='detail'),
    path('add/', ReviewCreateView.as_view(), name='add'),
]