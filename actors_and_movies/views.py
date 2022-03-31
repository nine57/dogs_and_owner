import json

from django.http    import JsonResponse
from django.views   import View

from .models        import Actor, Movie

# Views here.
class ActorView(View):
    def post(self, request):
        data = json.loads(request.body)

        actors = Actor.objects.create(
            first_name    = data['first_name'],
            last_name     = data['last_name'],
            date_of_birth = data['date_of_birth'],
        )

        return JsonResponse ({'message' : 'created'}, status=201)

    def get(self, request):
        actors = Actor.objects.all()
        result = []

        for actor in actors:
            movies = actor.movie.values('title')
            acting_movies = []
            for movie in movies:
                acting_movies.append(movie)
            result.append({
                "first_name"    : actor.first_name,
                "last_name"     : actor.last_name,
                "date_of_birth" : actor.date_of_birth,
                "movies"        : acting_movies,
            })

        return JsonResponse({"result" : result}, status=200)

class MovieView(View):
    def post(self, request):
        data = json.loads(request.body)

        movies = Movie.objects.create(
            title        = data['title'],
            release_date = data['release_date'],
            running_time = data['running_time']
        )

        return JsonResponse({'message' : 'created'}, status=201)

    def get(self, request):
        movies = Movie.objects.all()
        result = []

        for movie in movies:
            actors = movie.actor_set.values('first_name','last_name')
            actor_in_movie = []
            for actor in actors:
                actor_in_movie.append(actor)
            result.append({
                "title"        : movie.title,
                "release_date" : movie.release_date,
                "running_time" : movie.running_time,
                "actors"       : actor_in_movie
            })

        return JsonResponse({"result" : result}, status=200)