class Genre:
    __genre_name: str

    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str or genre_name == "\n":
            self.__genre_name = None
        else:
            sanitized_genre_name = genre_name.strip()
            self.genre_list = sanitized_genre_name.split(",")
            self.__genre_name = self.genre_list[0]
            if len(self.genre_list) > 1:
                self.subgenres = self.genre_list[1:]

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        return self.__genre_name == other.__genre_name

    # noinspection PyUnboundLocalVariable
    def __lt__(self, other):
        genre_list = [self, other]
        if hasattr(self, "genre_name") and self.genre_name is not None \
                and hasattr(other, "genre_name") and other.genre_name is not None:
            if self.__genre_name != other.__genre_name:
                genre_list.sort(key=lambda x: x.__genre_name)
            elif self.subgenres != other.subgenres:
                genre_list.sort(key=lambda x: x.subgenres)
        if self == genre_list[0]:
            return True
        else:
            return False

    def __hash__(self):
        if hasattr(self, "genre_name"):
            has_subgenres = hasattr(self, "subgenres")
            hash_string = f"{self.genre_name} - {has_subgenres}"
            return hash(hash_string)
        else:
            return None


# noinspection PyUnusedLocal,PyUnusedLocal
class TestGenreMethods:

    def test_innit(self):
        genre1 = Genre("Horror")
        genre2 = Genre("")
        genre3 = Genre("sci-fi")
        genre4 = Genre("Action,Adventure,Sci-Fi")
        genre5 = Genre("Adventure,Drama,Romance")

        assert repr(genre1) == "<Genre Horror>"
        assert repr(genre2) == "<Genre None>"
        assert repr(genre3) == "<Genre sci-fi>"
        assert repr(genre4) == "<Genre Action>"
        assert genre5.subgenres == ['Drama', 'Romance']
        assert genre1.__eq__(genre2) is False
        assert genre1.__eq__(genre1) is True
        assert genre1.__lt__(genre2) is True
        assert genre1.__lt__(genre3) is True
