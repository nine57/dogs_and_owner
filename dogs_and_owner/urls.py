from django.urls import path, include

urlpatterns = [
    path('dogs_and_owner', include('owner.urls')),
    path('actors_and_movies', include('actors_and_movies.urls'))
]