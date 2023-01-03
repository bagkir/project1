from django.shortcuts import render, get_object_or_404
from .models import Movie
# Create your views here.

def show_all_movie(request):
    movies = Movie.objects.all()
    for movie in movies:
        movie.save()

    return render(request, 'movie_app/all_movies.html', context={'movies': movies})


def show_the_movie(request, name_of_movie):
    movie = Movie.objects.get(name=name_of_movie)
    return render(request, 'movie_app/movie.html', context={'movie': movie})


def show_the_movie_by_number(request, slug_of_movie: int):
    movie = get_object_or_404(Movie, slug=slug_of_movie)
    return render(request, 'movie_app/movie.html', context={'movie': movie})

