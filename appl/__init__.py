import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# from wtforms import Form
import appl.adaptors.repository as repo
from appl.adaptors import memory_repository, database_repository
from appl.adaptors.orm import metadata, map_model_to_tables



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy.pool import NullPool

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    data_path = os.path.join('appl', 'adaptors', 'datafiles')
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']
    database_echo = app.config['SQLALCHEMY_ECHO']
    database_engine = create_engine(database_uri, connect_args={"check_same_thread": False}, poolclass=NullPool,
                                    echo=database_echo)

    if app.config['TESTING'] == 'True' or len(database_engine.table_names()) == 0:
        print("REPOPULATING DATABASE")
        # For testing, or first-time use of the web application, reinitialise the database.
        clear_mappers()
        metadata.create_all(database_engine)  # Conditionally create database tables.
        for table in reversed(metadata.sorted_tables):  # Remove any data from the tables.
            database_engine.execute(table.delete())

        # Generate mappings that map domain model classes to the database tables.
        map_model_to_tables()

        database_repository.populate(database_engine, data_path)
    else:
        # Solely generate mappings that map domain model classes to the database tables.
        map_model_to_tables()

    @app.route("/", methods=["POST", "GET"])
    def home():
        movie_list = repo.repo_instance.get_movies()
        actor_list = repo.repo_instance.get_actors()
        director_list = repo.repo_instance.get_directors()
        genre_list = repo.repo_instance.get_genres()
        review_list = repo.repo_instance.get_reviews()
        watchlist_list = repo.repo_instance.get_watchlists()
        return render_template("home.html", movies=movie_list, actors=actor_list, directors=director_list, genres=genre_list, reviews=review_list, watchlists=watchlist_list)



    @app.route("/login")
    def login():
        return render_template("login.html")


    return app