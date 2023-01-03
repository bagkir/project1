from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_of_movie>', views.show_the_movie_by_number, name='movie-slug'),
    path('movie/<name_of_movie>', views.show_the_movie, name='movie-name'),
]
