
from django.views.generic import ListView, DetailView, CreateView
from .models import Review
from .forms import ReviewForm

class ReviewListView(ListView):
	model = Review
	template_name = 'reviews/review_list.html'
	context_object_name = 'reviews'

class ReviewDetailView(DetailView):
	model = Review
	template_name = 'reviews/review_detail.html'
	context_object_name = 'review'

class ReviewCreateView(CreateView):
	model = Review
	form_class = ReviewForm
	template_name = 'reviews/review_form.html'
	success_url = '/reviews/'
