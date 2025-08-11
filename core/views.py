
from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from movies.models import Movie
from reviews.models import Review
from django.db.models import Avg, Count

class TopRatedView(ListView):
	model = Movie
	template_name = 'core/top_rated.html'
	context_object_name = 'movies'

	def get_queryset(self):
		return Movie.objects.order_by('-rating')[:10]


class HomeView(TemplateView):
	template_name = 'core/home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['movies'] = Movie.objects.order_by('-id')  # Show all movies
		return context


class TrendingView(ListView):
	model = Movie
	template_name = 'core/trending.html'
	context_object_name = 'movies'

	def get_queryset(self):
		# Trending: top 10 movies by average rating (with at least 1 review)
		return Movie.objects.annotate(avg_rating=Avg('reviews__rating'), num_reviews=Count('reviews')).filter(num_reviews__gt=0).order_by('-avg_rating', '-num_reviews')[:10]

class SearchView(ListView):
	model = Movie
	template_name = 'core/search.html'
	context_object_name = 'movies'

	def get_queryset(self):
		query = self.request.GET.get('q')
		qs = Movie.objects.all()
		if query:
			qs = qs.filter(title__icontains=query)
		return qs

def analytics_view(request):
	total_movies = Movie.objects.count()
	total_reviews = Review.objects.count()
	avg_rating = Review.objects.aggregate(Avg('rating'))['rating__avg']
	top_movies = Movie.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')[:5]
	return render(request, 'core/analytics.html', {
		'total_movies': total_movies,
		'total_reviews': total_reviews,
		'avg_rating': avg_rating,
		'top_movies': top_movies,
	})
