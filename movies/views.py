
from django.views.generic import ListView, DetailView, CreateView
from .models import Movie
from .forms import MovieForm

class MovieListView(ListView):
	model = Movie
	template_name = 'movies/movie_list.html'
	context_object_name = 'movies'

class MovieDetailView(DetailView):
	model = Movie
	template_name = 'movies/movie_detail.html'
	context_object_name = 'movie'

class MovieCreateView(CreateView):
	model = Movie
	form_class = MovieForm
	template_name = 'movies/movie_form.html'
	success_url = '/movies/'
