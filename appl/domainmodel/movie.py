from appl.domainmodel.actor import Actor
from appl.domainmodel.director import Director

"""
Check all arguments and return types

check for corner cases




"""

# noinspection PyStatementEffect
class Movie:
    __title: str
    __director: Director
    __actors: list
    __runtime_minutes: int
    __genres: list
    __description: str
    __rank: int

    def __init__(self, title: str, release_year: int):
        self.__director = None
        self.__actors = None
        self.__runtime_minutes = None
        self.__genres = None
        self.__description = None
        self.__release_year = None
        self.__id = None

        if title == "" or type(title) is not str or title == "\n":
            self.__title = None
            if release_year < 1900 or not isinstance(release_year, int):
                self.release_year = None
        else:
            self.__title = title.strip()
            if release_year >= 1900:  # and isinstance():
                self.release_year = release_year
            else:
                self.release_year = None
        self.__release_year = self.release_year
        self.__id = self.__title + str(self.release_year)
    @property
    def director(self):
        return self.__director.__repr__()

    @director.setter
    def director(self, new_director):
        if isinstance(new_director, Director):
            self.__director = new_director
        elif isinstance(new_director, list):
            if len(new_director) > 1:
                self.__director = new_director[0]
        elif isinstance(new_director, str):
            self.__director = Director(new_director)
        else:
            self.__director = None

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, new_rank: int):
        if isinstance(new_rank, int):
            self.__rank = new_rank

    @property
    def description(self):
        if self.__description is None:
            return f"Release Yeae{self.release_year}\n Directed by:{self.__director}"
        return self.description

    @description.setter
    def set_description(self, new_description):
        if isinstance(new_description, str):
            self.description = new_description
        else:
            self.description = None

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, new_actors):
        self.__actors.append(new_actors)

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, new_genres):
        self.__genres = new_genres

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, new_runtime_minutes):
        assert isinstance(new_runtime_minutes, int)
        if new_runtime_minutes <= 0:
            raise ValueError
        else:
            self.__runtime_minutes = new_runtime_minutes

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        if new_description is not None:
            self.__description = new_description.strip()

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, new_title):
        if new_title is not None:
            self.__title == new_title.strip()

    def __repr__(self):
        return f"<Movie {self.__title}, {self.release_year}>"

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __lt__(self, other):
        if hasattr(self, "title") and hasattr(other, "title") \
                and hasattr(self, "release_year") and hasattr(other, "release_year"):
            movie_list = [self, other]
            if self.title != other.title:
                movie_list.sort(key=lambda x: x.title)
                if self == movie_list[0]:
                    return True
                else:
                    return False
            else:
                if self.release_year != other.release_year:
                    movie_list.sort(key=lambda x: x.release_year)
                    if self == movie_list[0]:
                        return True
                    else:
                        return False

    def __hash__(self):
        hash_string = self.__title + str(self.release_year)
        return hash(hash_string)

    def add_actor(self, new_actor):
        if self.__actors is None:
            self.__actors = list()
            self.__actors.append(new_actor)
        else:
            if self.__actors is not None and new_actor not in self.__actors:
                self.__actors.append(new_actor)

    def remove_actor(self, actor_to_remove):
        if self.__actors is not None and actor_to_remove in self.__actors:
            self.__actors.remove(actor_to_remove)
        # else:
        #     print(f"Actor {actor_to_remove} is not present in this movie")

    def add_genre(self, genre_to_add):
        if self.__genres is None:
            self.__genres = list()
            self.__genres.append(genre_to_add)
        else:
            if self.__genres is not None and genre_to_add not in self.__genres:
                self.__genres.append(genre_to_add)

    def remove_genre(self, genres_to_remove):
        if self.__genres is not None and genres_to_remove in self.__genres:
            self.__genres.remove(genres_to_remove)
        # else:
        #     print(f"Genre {genres_to_remove} is not present in this movie")

    def get_title(self):
        return self.__title


# noinspection SpellCheckingInspection
class TestMovieMethods:
    def test_init(self):
        movie = Movie("Moana", 2016)
        movie1 = Movie("Joana", 2016)
        assert repr(movie) == "<Movie Moana, 2016>"
        director = Director("Ron Clements")
        movie.director = director
        assert movie.director == "<Director Ron Clements>"
        assert movie.__eq__(movie1) is False
        director_list = [Director("James Cameron"), Director("Johnny Big")]
        movie.director = director_list
        assert movie.director == "<Director James Cameron>"

        actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
        for actor in actors:
            movie.add_actor(actor)
        print(movie.actors)
        assert movie.actors == [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"),
                                Actor("Temuera Morrison")]
        assert movie.runtime_minutes is None
        movie.runtime_minutes = 107
        assert movie.runtime_minutes == 107
