
# Movie Rating System

The Movie Rating System allows users to manage movies and rate them. It provides features such as user authentication, adding movies, listing movies, rating movies, and searching movies.



## Features

- User login
- Add movie
- Rate movie
- Search Movie


## Tech Stack

**Client:** HTML, CSS

**Server:** Python, Django, DRF


## Installation

Clone the repository:

```bash
  https://github.com/fahadfoysal/movie-rating

```
Install dependencies:
```bash
  pip install -r requirements.txt

``` 
Apply database migrations:

```bash
  python manage.py migrate

```
Run the development server:
```bash
  python manage.py runserver

``` 
## Usage/Examples

```
Access the Django admin panel at http://localhost:8000/admin/ to manage movies and ratings.

Use the provided APIs for user authentication, adding movies, listing movies, rating movies, and searching movies.

http://localhost:8000 - Front-end View
http://localhost:8000/api - api for json response

## API Endpoints

- Login API: `/api/login/` (POST)
- Add Movie API: `/api/add_movie/` (POST)
- List Movies API: `/api/movies/` (GET)
- Rate Movie API: `/api/rate_movie/` (POST)
- Search Movie API: `/api/search_movie/` (GET)
- Movie Detail API: `/api/movie_detail/<movie_id>/` (GET)

## Authentication

Token-based authentication is used for API endpoints. After logging in, obtain a token and include it in the header of subsequent requests as follows:


