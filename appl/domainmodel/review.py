from datetime import *

from appl.domainmodel.movie import Movie


class Review:
    __review_id: int
    __movie: Movie
    __review_text: str
    __rating: int
    __timestamp: str
    __movie_title = str

    def __init__(self, movie, review_text: str, rating: int):
        self.__timestamp = datetime.now()
        if isinstance(movie, str):
            movie_object_tuple = string_to_movie(movie)
            self.__movie = Movie(movie_object_tuple[0], movie_object_tuple[1])
            self.__movie_title = self.__movie.title

        if movie is not None and isinstance(movie, Movie):
            self.__movie = movie
            self.__movie_title = movie.title.strip("<>")

        if review_text is not None and isinstance(review_text, str) and review_text != "" and review_text != "\n":
            self.__review_text = review_text
        if rating is not None and isinstance(rating, int):
            if 0 < rating <= 10:
                self.__rating = rating
            else:
                self.__rating = None
        self.__review_id = self.__hash__()
    @property
    def review(self) -> str:
        return self.__movie_title

    def __repr__(self):
        return f"<Review {self.__movie_title}, {self.__movie.release_year}; " \
               f"rated {self.__rating} on {self.__timestamp}>"

    def __eq__(self, other):
        if self.__movie_title == other.__movie_title and self.__rating == other.__rating \
                and self.__review_text == other.__review_text:  # and self.__timestamp == other.__timestamp:
            return True
        else:
            return False

    def __hash__(self):
        return hash(f"{self.__movie}{self.__rating}{self.__review_text}")

    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, new_movie):
        if isinstance(new_movie, Movie):
            self.__movie = new_movie

    @property
    def review_text(self):
        return self.__review_text

    @review_text.setter
    def review_text(self, new_review_text):
        if new_review_text is not None and isinstance(new_review_text,
                                                      str) and new_review_text != "" and new_review_text != "\n":
            self.__review_text = new_review_text

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, new_rating):
        if new_rating is not None and isinstance(new_rating, int) and 0 < new_rating <= 10:
            self.__rating = new_rating

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, new_timestamp):
        if isinstance(new_timestamp, str):
            self.__timestamp = new_timestamp


def string_to_movie(movie_string):
    movie_title_elements = [item.strip() for item in movie_string.split(",")]
    if len(movie_title_elements) == 2:
        movie_title = movie_title_elements[0]
        movie_release_year = int(movie_title_elements[1])
        return movie_title, movie_release_year



#
# movie1 = "James Bond, 2016"
# review_text1 = "This movie was very tame."
# rating1 = 8
# review1 = Review(movie1, review_text1, rating)
# print(review1.movie)
# print("Review: {}".format(review1.review_text))
# print("Rating: {}".format(review1.rating))
# print(review1)
#
# movie2 = Movie("James Bond", 2016)
# review_text2 = "This movie was very tame."
# rating2 = 8
# review2 = Review(movie2, review_text2, rating2)
# print(review2.movie)
# print("Review: {}".format(review2.review_text))
# print("Rating: {}".format(review2.rating))
# print(review2)
#
# print("hash review1", review1.__hash__())
# print("hash review2", review2.__hash__())
#
# print(review1.__eq__(review2))
#
# print(review1.review_text)
