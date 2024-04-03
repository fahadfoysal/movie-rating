from django.contrib import admin
from .models import CustomUser, Movie, Rating

admin.site.register(CustomUser)
admin.site.register(Movie)
admin.site.register(Rating)