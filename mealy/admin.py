from django.contrib import admin
from .models import Guest, Movie, Reservation, post

admin.site.register(Guest)
admin.site.register(Movie)
admin.site.register(Reservation)
admin.site.register(post)
