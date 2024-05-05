from db.models import Movie, Genre, Actor


def get_movies(genres_ids: list = None, actors_ids: list = None) -> Movie:
    all_movies = Movie.objects.all()
    if genres_ids and actors_ids:
        all_movies = all_movies.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        )
    elif genres_ids:
        all_movies = all_movies.filter(genres__id__in=genres_ids)
    elif actors_ids:
        all_movies = all_movies.filter(actors__id__in=actors_ids)
    return all_movies.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if actors_ids:
        actors = Actor.objects.filter(pk__in=actors_ids)
        movie.actors.set(actors)
    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)
    return movie
