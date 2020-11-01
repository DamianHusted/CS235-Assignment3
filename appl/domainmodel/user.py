from datetime import datetime

from appl.domainmodel.movie import Movie
from werkzeug.security import generate_password_hash


class User:
    __username: str
    __password: str
    __watched_movies: list
    __reviews: list
    __time_spent_watching_movies_minutes: int
    __complete_viewing_history: dict
    __user_id: int

    __user_first_name: str
    __user_last_name: str
    __user_age: int
    __user_email: str
    __user_consent = bool

    def __init__(self, username: str, password: str, id: str, first_name: str, last_name: str, age: int,
                 email: str, consent: bool):
        if username is None or not isinstance(username, str) or username == "" or username == "\n":
            self.__username = None
        else:
            username = username.strip()
            self.__username = username.lower()
        if password is None or not isinstance(password, str) or password == "\n" or password == "":
            self.__password = None
        else:
            self.__password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
        self.__complete_viewing_history = {"Complete history": [], "Total viewing time": 0, "Unique movies viewed": [],
                                           "Reviews": []}

        if id is None:
            self.__timestamp = datetime.now()
            self.__user_id = hash(f"{self.__username}")
        else:
            self.__user_id = id
        self.__user_first_name = first_name
        self.__user_last_name = last_name
        self.__user_age = age
        self.__user_email = email
        self.__user_consent = consent
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    # @property
    # def username(self):
    #     return self.__username

    # @username.setter
    # def username(self, new_user_name):
    #     if new_user_name is not None and isinstance(new_user_name,
    #                                                 str) and new_user_name != "" and new_user_name != "\n":
    #         self.__username = new_user_name

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, new_user_name):
        if new_user_name is not None and isinstance(new_user_name,
                                                    str) and new_user_name != "" and new_user_name != "\n":
            self.__username = new_user_name

    @property
    def user_first_name(self):
        return self.user_first_name

    @user_first_name.setter
    def user_first_name(self, new_first_name):
        if new_first_name is not None and isinstance(new_first_name,
                                                     str) and new_first_name != "\n" and new_first_name != "":
            self.__user_first_name = new_first_name

    @property
    def user_last_name(self):
        return self.user_last_name

    @user_last_name.setter
    def user_last_name(self, new_last_name):
        if new_last_name is not None and isinstance(new_last_name,
                                                    str) and new_last_name != "\n" and new_last_name != "":
            self.__user_last_name = new_last_name

    @property
    def user_age(self):
        return self.user_age

    @user_age.setter
    def user_age(self, new_age):
        if new_age is not None and isinstance(new_age, int) and new_age != "\n" and new_age != "":
            self.__user_age = new_age

    @property
    def user_consent(self):
        return self.user_consent

    @user_consent.setter
    def user_consent(self, new_consent):
        if new_consent is not None and isinstance(new_consent, bool) and new_consent != "\n" and new_consent != "":
            self.__user_consent = new_consent

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if new_password is not None and isinstance(new_password, str) and new_password != "\n" and new_password != "":
            self.__password = generate_password_hash(new_password, method='pbkdf2:sha256', salt_length=16)

    # # for added_password policy consider the following: # #

    # if len(password) < 8:
    #     print("Password must be at least 8 characters long")
    #     pass
    # non_alphanumeric_characters = 0
    # uppercase_characters = 0
    # lowercase_characters = 0
    # digits = 0
    # for index in range(len(password)):
    #     if password[index].isnumeric():
    #         digits += 1
    #         index += 1
    #     elif not password[index].isalnum():
    #         non_alphanumeric_characters += 1
    #         index += 1
    #     elif password[index].islower():
    #         lowercase_characters += 1
    #         index += 1
    #     elif password[index].isupper():
    #         uppercase_characters += 1
    #         index += 1
    #     else:
    #         index += 1
    # if non_alphanumeric_characters < 1 or uppercase_characters < 1 or lowercase_characters < 1 or digits < 1:
    #     print("Password must contain at least: 1 upper-case character, 1 lower-case character, "
    #           "1 digit and 1 non-alphamumeric character")
    #     pass
    # else:
    #     self.__password = password
    @property
    def user_id(self):
        return self.__user_id

    @property
    def watched_movies(self):
        return self.__watched_movies

    @watched_movies.setter
    def watched_movies(self, new_watched_movies):
        if isinstance(new_watched_movies, list):
            self.__watched_movies = new_watched_movies
            self.__complete_viewing_history["Unique movies viewed"] = new_watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, new_review_list):
        if isinstance(new_review_list, list):
            self.__reviews = new_review_list

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, replacement_time):
        if replacement_time >= 0:
            self.__time_spent_watching_movies_minutes = replacement_time

    @property
    def complete_viewing_history(self):
        return self.__complete_viewing_history

    @complete_viewing_history.setter
    def complete_viewing_history(self, new_viewing_history):
        if new_viewing_history is not None and isinstance(new_viewing_history, dict):
            self.__complete_viewing_history = new_viewing_history

    def __repr__(self):
        return f"<User {self.__username}>"

    def __eq__(self, other_user):
        if self.__username == other_user.__username:
            return True
        else:
            return False

    def __lt__(self, other_user):
        return self.username < other_user.__username

    def __hash__(self):
        return hash(self.username)

    def watch_movie(self, movie: Movie):
        if movie not in self.__watched_movies:
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes
            self.__complete_viewing_history["Complete history"].append(movie)
            self.__complete_viewing_history["Total viewing time"] += self.__time_spent_watching_movies_minutes
            self.__complete_viewing_history["Unique movies viewed"].append(movie)
        else:
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes
            self.__complete_viewing_history["Complete history"].append(movie)
            self.__complete_viewing_history["Total viewing time"] += self.__time_spent_watching_movies_minutes
            self.__complete_viewing_history["Unique movies viewed"].append(movie)

    def add_review(self, review_to_add):
        if review_to_add not in self.__reviews:
            self.__reviews.append(review_to_add)
            self.__complete_viewing_history["Reviews"].append(review_to_add)

#
# user0 = User("slowloris", "One Direction is da best musik")
# user1 = User("slowloris", "DEEEEEEEEEEJAAAAAAAAAAY KHAAAAALEED!")
# print(user0.__hash__())
# print(user1.__hash__())
