import abc
from appl.domainmodel.actor import Actor
from appl.domainmodel.movie import Movie
from appl.domainmodel.director import Director
from appl.domainmodel.genre import Genre
from appl.domainmodel.review import Review
from appl.domainmodel.user import User
from appl.domainmodel.watchlist import Watchlist


repo_instance = None


class RepositoryException(Exception):
    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get_movies(self, movie_list: list):
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self, user: User):
        """:param user """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        """:returns None if no user with the given username is found"""
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """Adds a movie to the repository"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, movie) -> Movie:
        """Returns Watchlist"""
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        """Adds a actor to the repository"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_actor(self, actor) -> Actor:
        """Returns Actor"""
        raise NotImplementedError

    @abc.abstractmethod
    def add_director(self, director: Director):
        """Adds a director to the repository"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_director(self, director) -> Director:
        """Returns Director"""
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        """Adds genre to repo"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_genre(self, genre) -> Genre:
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review: Review):
        """Adds a review to the repository"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_review(self, review) -> Review:
        """Returns Review"""
        raise NotImplementedError

    @abc.abstractmethod
    def add_watchlist(self, watchlist: Watchlist):
        """Adds a watchlist to the repository"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_watchlists(self, watchlist) -> Watchlist:
        """Returns Watchlist"""
        raise NotImplementedError

    # @abc.abstractmethod
    # def get_number_of_movies(self) -> int:
    #     """Returns the number of movies in the 'database/repo' """
    #     raise NotImplementedError
    #
    # @abc.abstractmethod
    # def get_number_of_directors(self) -> int:
    #     """Returns the number of directors in the 'database/repo' """
    #     raise NotImplementedError
    #
    # @abc.abstractmethod
    # def get_number_of_actors(self) -> int:
    #     """Returns the number of actors in the 'database/repo' """
    #     raise NotImplementedError
    #
    # @abc.abstractmethod
    # def get_number_of_genres(self) -> int:
    #     """Returns the number of genres in the 'database/repo' """
    #     raise NotImplementedError
    #
    # @abc.abstractmethod
    # def get_number_of_reviews(self) -> int:
    #     """Returns the number of reviews in the 'database/repo' """
    #     raise NotImplementedError
    #
    # @abc.abstractmethod
    # def get_number_of_watchlists(self) -> int:
    #     """Returns the number of watchlists in the 'database/repo' """
    #     raise NotImplementedError
