from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from .models import Movie, Rating
from django.db.models import Avg
from .forms import MovieForm

@login_required
def movie_list(request):
    movies = Movie.objects.annotate(avg_rating=Avg('ratings__rating'))
    return render(request, 'movie/movie_list.html', {'movies': movies})

@login_required
def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    avg_rating = movie.ratings.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'movie/movie_detail.html', {'movie': movie, 'avg_rating': avg_rating})


@login_required
def rate_movie(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_id)
        rating_value = request.POST['rating']
        Rating.objects.create(user=request.user, movie=movie, rating=rating_value)
    return redirect('movie_list')

@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie/add_movie.html', {'form': form})

@login_required
def movie_search(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(name__icontains=query)
    else:
        movies = Movie.objects.all()
    return render(request, 'movie/movie_search.html', {'movies': movies, 'query': query})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'movie/users_register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email,
                                password=password)
            if user is not None:
                login(request, user)
                return redirect('movie_list')
    else:
        form = UserLoginForm()
    return render(request, 'movie/login.html', {'form':form})


def user_logout(request):
    logout(request)
    return render(request, 'movie/logout.html')