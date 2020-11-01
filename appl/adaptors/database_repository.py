import csv
import os

from datetime import date
from typing import List

from sqlalchemy import desc, asc
from sqlalchemy.engine import Engine
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from werkzeug.security import generate_password_hash

from sqlalchemy.orm import scoped_session
from flask import _app_ctx_stack

from appl.adaptors.repository import AbstractRepository
from appl.domainmodel.actor import Actor
from appl.domainmodel.director import Director
from appl.domainmodel.genre import Genre
from appl.domainmodel.review import Review
from appl.domainmodel.movie import Movie
from appl.domainmodel.user import User
from appl.domainmodel.watchlist import Watchlist

from appl.datafilereaders.movie_file_csv_reader import MovieFileCSVReader


class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        # this method can be used e.g. to allow Flask to start a new session for each http request,
        # via the 'before_request' callback
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def close_current_session(self):
        if not self.__session is None:
            self.__session.close()


class SqlAlchemyRepository(AbstractRepository):

    def get_movie(self, movie) -> Movie:
        pass

    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    def get_movies(self):
        movies = self._session_cm.session.query(Movie).all()
        return movies

    def add_user(self, user: User):
        with self._session_cm as scm:
            scm.session.add(user)
            scm.commit()

    def get_user(self, username):
        user = None
        try:
            user = self._session_cm.session.query(User).filter_by(__username=username).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return user

    def get_user_firstname(self, user_id):
        user_firstname = None
        try:
            user_firstname = self._session_cm.session.query(User).filter_by(__user_id=user_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return user_firstname

    def get_user_lastname(self, user_id):
        user_lastname = None
        try:
            user_lastname = self._session_cm.session.query(User).filter_by(user_id=user_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return user_lastname

    def get_user_password(self, username):
        user_password = None
        try:
            user_password = self._session_cm.session.query(User).filter_by(__username=username).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return user_password

    def get_user_watched_movies(self, username) -> List[Movie]:
        user = None
        try:
            user = self._session_cm.session.query(User).filter_by(__username=username).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return user.watched_movies

    def get_user_reviews(self, username):
        user = None
        try:
            user = self._session_cm.session.query(User).filter_by(username=username).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return user.reviews

    def get_user_id(self, username):
        user = None
        try:
            user = self._session_cm.session.query(User).filter_by(__username=username).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return user.user_id

    def get_user_age(self, username):
        user = None
        try:
            user = self._session_cm.session.query(User).filter_by(__username=username).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return user.user_age

    def get_user_email(self, username):
        user = None
        try:
            user = self._session_cm.session.query(User).filter_by(__username=username).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return user.email

    def get_user_consent(self, username):
        user = None
        try:
            user = self._session_cm.session.query(User).filter_by(__username=username).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return user.user_consent

    def add_movie(self, movie: Movie):
        with self._session_cm as scm:
            scm.session.add(movie)
            scm.commit()

    def get_movie_title(self, movie_id):
        movie = None
        try:
            movie = self._session_cm.session.query(Movie).filter_by(__id=movie_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return movie.movie_title

    def get_movie_director(self, movie_id):
        movie = None
        try:
            movie = self._session_cm.session.query(Movie).filter_by(__id=movie_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return movie.director

    # def get_movie_director_by_title(self, movie_title):
    #     movie = None
    #     try:
    #         movie = self._session_cm.session.query(Movie).filter_by(__title=movie_title).one()
    #     except NoResultFound:
    #         # Ignore any exception and return None.
    #         pass
    #     return movie.director

    def get_movie_runtime(self, movie_id) -> Movie:
        movie = None
        try:
            movie = self._session_cm.session.query(Movie).filter_by(__id=movie_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return movie.movie_runtime

    def get_movie_genres(self, movie_id) -> Movie:
        movie = None
        try:
            movie = self._session_cm.session.query(Movie).filter_by(__id=movie_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return movie.genres

    def get_movie_description(self, movie_id):
        movie = None
        try:
            movie = self._session_cm.session.query(Movie).filter_by(__id=movie_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return movie.description

    def get_movie_rank(self, movie_id):
        movie = None
        try:
            movie = self._session_cm.session.query(Movie).filter_by(__id=movie_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return movie.rank

    def add_review(self, review: Review):
        with self._session_cm as scm:
            scm.session.add(review)
            scm.commit()


    def get_review_text(self, review_id):
        review = None
        try:
            review = self._session_cm.session.query(Review).filter_by(__review_id=review_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return review.review_text

    def get_review_rating(self, review_id):
        review = None
        try:
            review = self._session_cm.session.query(Review).filter_by(__review_id=review_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return review.rating

    def get_review_movie_title(self, review_id):
        review = None
        try:
            review = self._session_cm.session.query(Review).filter_by(__review_id=review_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return review.movie_title

    def get_review_timestamp(self, review_id):
        review = None
        try:
            review = self._session_cm.session.query(Review).filter_by(__review_id=review_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return review.timestamp


    def add_genre(self, genre: Genre):
        with self._session_cm as scm:
            scm.session.add(genre)
            scm.commit()

    def get_genre(self, genre_id):
        genre = None
        try:
            genre = self._session_cm.session.query(Genre).filter_by(_genre_id=genre_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return genre.genre_name

    def get_movie_genre(self, movie_id):
        movie = None
        try:
            movie = self._session_cm.session.query(Movie).filter_by(__id=movie_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return movie.genre

    def add_actor(self, actor: Actor):
        with self._session_cm as scm:
            scm.session.add(actor)
            scm.commit()

    def get_actor(self, actor_id):
        actor = None
        try:
            actor = self._session_cm.session.query(Actor).filter_by(__=actor).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass

    def get_actor_firstname(self, actor_id):
        actor = None
        try:
            actor = self._session_cm.session.query(Actor).filter_by(__actor_id=actor_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return actor.firstname

    def get_actor_lastname(self, actor_id):
        actor = None
        try:
            actor = self._session_cm.session.query(Actor).filter_by(__actor_id=actor_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return actor.lastname

    def get_actor_middlenames(self, actor_id):
        actor = None
        try:
            actor = self._session_cm.session.query(Actor).filter_by(__actor_id=actor_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return actor.middlenames

    def add_director(self, director: Director):
        with self._session_cm as scm:
            scm.session.add(director)
            scm.commit()

    def get_director(self, director_id):
        director = None
        try:
            director = self._session_cm.session.query(Director).filter_by(__id=director_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return director.full_name


    def get_director_firstname(self, director_id):
        director = None
        try:
            director = self._session_cm.session.query(Director).filter_by(__id=director_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return director.director_firstname

    def get_director_lastname(self, director_id):
        director = None
        try:
            director = self._session_cm.session.query(Director).filter_by(__id=director_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return director.director_lastname

    def add_watchlist(self, watchlist: Watchlist):
        with self._session_cm as scm:
            scm.session.add(watchlist)
            scm.commit()

    def get_watchlist(self, user_id):
        user = None
        try:
            user = self._session_cm.session.query(User).filter_by(__user_id=user_id).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return user.watchlist

    def populate(session_factory, data_path, data_filename):
        filename = os.path.join(data_path, data_filename)
        movie_file_reader = MovieFileCSVReader(filename)
        movie_file_reader.read_csv_file()
        session = session_factory()
        # This takes all movies from the csv file (represented as domain model objects) and adds them to the
        # database. If the uniqueness of directors, actors, genres is correctly
        # handled, and the relationships# are correctly set up in the ORM mapper,
        # then all associations will be dealt with as well!
        for movie in movie_file_reader.dataset_of_movies:
            session.add(movie)
            session.commit()