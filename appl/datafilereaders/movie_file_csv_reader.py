import csv
from appl.domainmodel.movie import Movie
from appl.domainmodel.genre import Genre
from appl.domainmodel.actor import Actor
from appl.domainmodel.director import Director


# noinspection DuplicatedCode
class MovieFileCSVReader:
    dataset_of_movies: list
    dataset_of_actors: set
    dataset_of_directors: set
    dataset_of_genres: set
    filename: str

    def __init__(self, file_name: str):
        self.__dataset_of_genres = set()
        self.__dataset_of_directors = set()
        self.__dataset_of_actors = set()
        self.__dataset_of_movies = list
        self.__file_name = file_name

    # noinspection PyUnusedLocal
    def read_csv_file(self):
        # noinspection SpellCheckingInspection
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            self.__dataset_of_movies = []
            self.__dataset_of_actors = set()
            self.__dataset_of_directors = set()
            self.__dataset_of_genres = set()
            index = 0
            for row in movie_file_reader:
                rank = row['Rank']
                title = row['Title']
                director = row['Director']
                actor = row['Actors']
                release_year = int(row['Year'])
                genre = row['Genre']

                genre_list = genre.split(",")
                genre_list = [Genre(item.strip()) for item in genre_list]

                for item in genre_list:
                    if item not in self.__dataset_of_genres:  # or len(self.__dataset_of_genres) == 0:
                        self.__dataset_of_genres.add(item)

                actor_list = actor.split(",")
                actor_list = [Actor(item.strip()) for item in actor_list]

                for item in actor_list:
                    if item not in self.__dataset_of_actors:  # or len(self.__dataset_of_actors) == 0:
                        self.__dataset_of_actors.add(item)

                movie_object = Movie(title, release_year)
                if movie_object not in self.__dataset_of_movies:  # or len(self.__dataset_of_movies) == 0:
                    self.__dataset_of_movies.append(movie_object)

                director_object = Director(director)
                if director_object not in self.__dataset_of_directors:  # or len(self.__dataset_of_directors) == 0:
                    self.__dataset_of_directors.add(director_object)

                index += 1

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    # @dataset_of_movies.setter
    # def dataset_of_movies(self, value):
    #     pass

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    # @dataset_of_actors.setter
    # def dataset_of_actors(self, value):
    #     pass

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    # @dataset_of_directors.setter
    # def dataset_of_directors(self, value):
    #     pass
    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

    # @dataset_of_genres.setter
    # def dataset_of_genres(self, value):
    #     pass

### Functions below are moved into the code above for efficiency/speed


# def add_actors(actors_string):
#     actor_list = actors_string.split(",")
#     # for item in actor_list:
#     #     item.strip()
#     return [Actor(item.strip()) for item in actor_list]
#
# def add_genres(genre_string):
#     genre_list = genre_string.split(",")
#     # for item in genre_list:
#     #     item.strip()
#     return [Genre(item.strip()) for item in genre_list]

# noinspection SpellCheckingInspection
