import csv

from appl.adaptors.repository import AbstractRepository
from appl.domainmodel.actor import Actor
from appl.domainmodel.director import Director
from appl.domainmodel.genre import Genre
from appl.domainmodel.review import Review
from appl.domainmodel.movie import Movie
from appl.domainmodel.user import User
from appl.domainmodel.watchlist import Watchlist


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self.__dataset_of_users = list()
        self.__dataset_of_movies = list()
        self.__dataset_of_directors = set()
        self.__dataset_of_actors = set()
        self.__dataset_of_genres = set()
        self.__dataset_of_reviews = list()
        self.__dataset_of_watchlists = list()
        self.__ranklist = list()

    def add_user(self, user: User):
        self.__dataset_of_users.append(user)

    def get_user(self, username) -> User:
        return next((user for user in self.__dataset_of_users if user.username == username), None)

    def add_movie(self, movie: Movie):
        self.__dataset_of_movies.append(movie)

    def get_movie(self, movie) -> Movie:
        return next((movie for movie in self.__dataset_of_movies if movie.movie_name == movie), None)

    def add_director(self, director: Director):
        self.__dataset_of_directors.add(director)

    def get_director(self, director) -> Director:
        return next((director for director in self.__dataset_of_directors if director.director_full_name == director),
                    None)

    def add_actor(self, actor: Actor):
        self.__dataset_of_actors.add(actor)

    def get_actor(self, actor) -> Actor:
        return next((actor for actor in self.__dataset_of_actors if actor.actor_namec == actor), None)

    def add_genre(self, genre: Genre):
        self.__dataset_of_genres.add(genre)

    def get_genre(self, genre) -> Genre:
        return next((genre for genre in self.__dataset_of_genres if genre.genre_name == genre), None)

    def add_review(self, review: Review):
        self.__dataset_of_reviews.append(review)

    def get_review(self, review) -> Review:
        return next((review for review in self.__dataset_of_reviews if review.review_text == review), None)

    def add_watchlist(self, watchlist: Watchlist):
        self.__dataset_of_watchlists.append(watchlist)

    def get_watchlist(self, watchlist) -> list:
        return self.__dataset_of_watchlists

    def get_number_of_movies(self):
        return len(self.__dataset_of_movies)

    def get_number_of_directors(self):
        return len(self.__dataset_of_directors)

    def get_number_of_actors(self):
        return len(self.__dataset_of_movies)

    def get_number_of_genres(self):
        return len(self.__dataset_of_genres)

    def get_number_of_reviews(self):
        return len(self.__dataset_of_reviews)

    def get_number_of_watchlists(self):
        return len(self.__dataset_of_watchlists)

    def get_movies(self):
        return self.__dataset_of_movies

    def get_actors(self):
        return self.__dataset_of_actors

    def get_directors(self):
        return self.__dataset_of_directors

    def get_genres(self):
        return self.__dataset_of_genres

    def get_reviews(self):
        return self.__dataset_of_reviews

    def get_watchlists(self):
        return self.__dataset_of_watchlists


def read_and_load_movie_file(file_name: str, repo: MemoryRepository):
    # noinspection SpellCheckingInspection
    with open(file_name, mode='r', encoding='utf-8-sig') as movie_file:
        movie_file_reader = csv.DictReader(movie_file)
        index = 0
        # noinspection DuplicatedCode
        for row in movie_file_reader:
            rank = row['Rank']
            title = row['Title']
            director = row['Director']
            actor = row['Actors']
            release_year = int(row['Year'])
            genre = row['Genre']
            description = row['Description']
            runtime = int(row['Runtime (Minutes)'])
            rating = row['Rating']
            movie_object = Movie(title, release_year)
            director_object = Director(director)
            movie_object.description = description
            movie_object.rank = rank
            movie_object.director = director_object
            movie_object.runtime_minutes = runtime
            movie_object.title = title
            movie_object.director = director
            








            genre_list = genre.split(",")
            genre_list = [Genre(item.strip()) for item in genre_list]

            for item in genre_list:
                movie_object.add_genre(item)
                repo.add_genre(item)

            actor_list = actor.split(",")
            actor_list = [Actor(item.strip()) for item in actor_list]

            for actor in actor_list:
                movie_object.add_actor(actor)

                repo.add_actor(actor)


            repo.add_movie(movie_object)


            repo.add_director(director_object)


            index += 1


def read_and_load_user_file(file_name: str, repo: MemoryRepository):
    with open(file_name, mode='r', encoding='utf-8-sig') as users_file:
        user_file_reader = csv.DictReader(users_file)
        user_list = []
        for row in user_file_reader:
            username = row['Username']
            user_id = row['User ID']
            user_pass = row['Password']
            user_first_name = row['First Name']
            user_last_name = row['Last Name']
            user_age = int(row['Age'])
            user_email = row['Email']
            user_consent = bool(row['Consent'])

            user_object = User(username, user_pass, user_id, user_first_name, user_last_name, user_age, user_email,
                               user_consent)
            user_list.append(user_object)
            repo.add_user(user_object)
    return user_list
