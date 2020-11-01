from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, DateTime, Boolean,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship
from lazy import *

metadata = MetaData()

from appl.adaptors.repository import AbstractRepository
from appl.domainmodel.actor import Actor
from appl.domainmodel.director import Director
from appl.domainmodel.genre import Genre
from appl.domainmodel.review import Review
from appl.domainmodel.movie import Movie
from appl.domainmodel.user import User
from appl.domainmodel.watchlist import Watchlist

actor = Table("actor", metadata,
              Column('actor_id', Integer, primary_key=True, nullable=False),
              Column('firstname', String, nullable=False),
              Column('middlenames', String, nullable=True),
              Column('lastname', String, nullable=True)
              )

# cast_person = Table("cast_person", metadata,
#                     Column('person_id', Integer, primary_key=True, nullable=False),
#                     Column('cast_id', Integer, primary_key=True, nullable=False)
#                     )
#
# colleague = Table("colleague", metadata,
#                   Column('colleague_list_id', Integer, primary_key=True, nullable=False)
#                   )
#
# colleague_list = Table("colleague_list", metadata,
#                        Column('colleague_id', Integer, primary_key=True, nullable=False),
#                        Column('colleague_list_id', Integer, primary_key=True, nullable=False)
#                        )

director = Table("director", metadata,
                 Column('director_id', Integer, primary_key=True, nullable=False),
                 Column('firstname', String),
                 Column('lastname', String)
                 )

genre = Table("genre", metadata,
              Column('genre_id', Integer, primary_key=True, autoincrement=True, nullable=False),
              Column('genre_name', String, primary_key=True, nullable=False)
              )

movie = Table("movie", metadata,
              Column('movie_id', String, primary_key=True, autoincrement=False),
              Column('movie_title', String, unique=False, nullable=False),
              Column('release_year', Integer, unique=False, nullable=False),
              Column('runtime', Integer, unique=False, nullable=False),
              Column("cast_id", Integer, unique=True, nullable=False),
              Column("director_id", Integer, ForeignKey('director.director_id'))
              )

#   Composite primary key with the two IDs
# movie_cast = Table("movie_cast", metadata,
#                    Column('cast_id', String, primary_key=True, nullable=False),
#                    Column('movie_id', String, nullable=False),
#                    )

# Composite primary key with the two IDs
# movie_director = Table("movie_director", metadata,
#                        Column('director_id', Integer, ForeignKey("director.director_id"), primary_key=True),
#                        Column('movie_id', String, ForeignKey("movie.movie_id"), primary_key=True)
#                        )

# movie_genre = Table("movie_genres", metadata,
#                     Column('movie_id', ForeignKey('movie.movie_id')),
#                     Column('genre_id', ForeignKey('genre.genre_id'))
#                     )
#
# movie_review = Table("movie_review", metadata,
#                      Table('review_id', ForeignKey('review.review_id')),
#                      Table('movie_id', ForeignKey('movie.movie_id'))
#                      )

# person = Table("person", metadata,
#                Column('person_id', Integer, primary_key=True, nullable=False),
#                Column('firstname', String, nullable=False),
#                Column('lastname', String)
#                )

review = Table("review", metadata,
               Column('review_id', Integer, primary_key=True, nullable=False),
               Column('review_text', String),
               Column('rating', Integer),
               Column('timestamp', DateTime),
               Column('movie_title', String),
               Column('user_id', Integer, ForeignKey('user.user_id'))
               )

user = Table("user", metadata,
             Column('user_id', Integer, primary_key=True, nullable=False),
             Column('firstname', String, nullable=False),
             Column('lastname', String, nullable=False),
             Column('password', String, nullable=False),
             Column('email', String, nullable=False),
             Column('name', String, nullable=False),
             Column('consent', Boolean, nullable=False),
             Column('review_list_id', Integer, nullable=True)
             )

# user_review = Table("user_review", metadata,
#                     Column('review_id', ForeignKey('review.review_id')),
#                     Column('user_id', ForeignKey('user.user_id'))
#                     )


# watchlist_movie = Table("watchlist_move", metadata,
#                         Column('watch_list_id', Integer, primary_key=True, nullable=False),
#                         Column('movie_id', String, primary_key=True, nullable=False),
#                         )

watchlist = Table("watchlist", metadata,
                   Column('watch_list_id', Integer, primary_key=True, nullable=False),
                   Column('user_id', Integer, ForeignKey('user.user_id')),
                   )


def map_model_to_tables():
    mapper(Actor, actor, properties={
        '_Actor__actor_id': actor.column.actor_id,
        '_Actor__firstname': actor.column.firstname,
        '_Actor__middlenames': actor.column.middlename,
        '_Actor__lastname': actor.column.lastname
    })

    mapper(Director, director, properties={
        '_Director__director_id': director.column.director_id,
        '_Director__director_firstname': director.column.firstname,
        '_Director__director_lastname': director.column.lastname
    })

    mapper(Movie, movie, properties={
        '_Movie__id': movie.column.movie_id,
        '_Movie__title': movie.column.movie_title,
        '_Movie__release_year': movie.column.release_year,
        '_Movie__runtime_minutes': movie.column.runtime,
        '_Movie__description': movie.column.description,
        '_Movie__director': relationship(Director, backref='_movie', lazy='select'),
        '_Movie__rank': movie.column.rank,
        '_Movie__genres': relationship(Genre, backref='_movie', lazy='select')
    })

    mapper(Review, review, properties={
        '_Review__review_id': review.column.review_id,
        '_Review__review_text': review.column.review_text,
        '_Review__rating': review.column.rating,
        '_Review__movie_title': relationship(Movie, backref='_review', lazy='select'),
        '_Review__timestamp': review.column.timestamp,

    })

    mapper(Genre, genre, properties={
        '_Genre__genre_id': genre.column.genre_id,
        '_Genre__genre_name': genre.column.genre_name

    })

    mapper(User, user, properties={
        '_User__username': user.column.username,
        '_User__password': user.column.password,
        '_User__watchlist': relationship(Watchlist, backref='_user'),
        '_User__reviews': relationship(Review, backref='_user'),
        '_User__user_id': user.column.user_id,
        '_User__user_first_name': user.column.firstname,
        '_User__user_last_name': user.column.lastname,
        '_User__user_age': user.column.age,
        '_User__user_email': user.column.email,
        '_User__user_consent': user.column.consent
    })

    # mapper(Director, movie_director, properties={
    #     '_Director__director_id': relationship(Director, backref='__director_id', lazy='select'),
    #     '_Movie__movie_id': relationship(Movie, backref='__movie_id', lazy='select'),
    # })
    #
    # mapper(Review, movie_review, properties={
    #     '_Review__review_id': relationship(Review, backref='_movie_review', lazy='select'),
    #     '_Movie__movie_id': relationship(Review, backref='_movie_review', lazy='select')
    #
    # })
