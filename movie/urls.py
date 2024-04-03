from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movies/<int:movie_id>/rate/', views.rate_movie, name='rate_movie'),
    path('movies/add/', views.add_movie, name='add_movie'),
    path('movies/search/', views.movie_search, name='movie_search'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]