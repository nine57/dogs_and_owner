from django.urls import path, include

urlpatterns = [
    path('actors_and_movies', include('actors_and_movies.urls'))
]
