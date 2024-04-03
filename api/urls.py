from django.urls import path
from .views import LoginAPIView,MovieListAPIView, RateMovieAPIView, AddMovieAPIView, SearchMovieAPIView, MovieDetailAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='api_login'),
    path('movies/', MovieListAPIView.as_view(), name='movie-list'),
    path('rate_movie/', RateMovieAPIView.as_view(), name='rate-movie'),
    path('add_movie/', AddMovieAPIView.as_view(), name='add-movie'),
    path('search_movie/', SearchMovieAPIView.as_view(), name='search-movie'),
    path('movie_detail/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
]