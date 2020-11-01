


class Director:
    __director_full_name: str
    __director_url: str

    def __init__(self, director_full_name: str):
        self.director_url = ""
        if director_full_name == "" or type(director_full_name) is not str or director_full_name == "\n":
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()
            # check for multiple names
            self.names_count = self.__director_full_name.count(" ") + 1
            # assign first and last names
            if self.names_count < 3:
                if " " in self.__director_full_name:
                    self.firstname = self.director_full_name[:self.__director_full_name.find(" ")]
                    self.lastname = self.director_full_name[self.__director_full_name.find(" ") + 1:]
                else:
                    # In case director goes by single name, first and last name will be assigned the same name for
                    # indexing purposes.
                    self.firstname = self.__director_full_name
                    self.lastname = self.director_full_name
            else:
                # assign first, middle and last names
                self.firstname = self.director_full_name[:self.__director_full_name.find(" ")]
                self.middlenames = self.__director_full_name[
                                   director_full_name.find(" ") + 1: self.__director_full_name.rfind("")]
                self.lastname = self.__director_full_name[self.__director_full_name.rfind(" ") + 1:]
            self.director_url = director_full_name.replace(" ", "_")
        self.__director_id = self.__hash__()
        self.__firstname = self.firstname
        self.__lastname = self.lastname


    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname
    @property
    def director_id(self):
        return self.__director_id

    @property
    def director_url(self):
        return self.__director_url

    @director_url.setter
    def director_url(self, value):
        self.__director_url = value

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        return self.__director_full_name == other.__director_full_name

    # noinspection DuplicatedCode
    def __lt__(self, other):
        # The following code is duplicated in the Actor class
        # Consider moving the following into a separate function or method accessible to both classes
        # Duplicate code start:
        name_list = [self, other]
        if hasattr(self, "firstname") and hasattr(other, "firstname"):
            if self.firstname != other.firstname:
                name_list.sort(key=lambda x: x.firstname)
            elif self.lastname != other.lastname:
                name_list.sort(key=lambda x: x.lastname)
            else:
                if self.middlenames.lower() == other.middlenames.lower():
                    name_list.sort(key=lambda x: x.middlenames)
            if self == name_list[0]:
                return True
            else:
                return False
            # Duplicate code end

    def __hash__(self):
        if hasattr(self, "firstname"):
            hash_string = f"{self.firstname[0]}.{self.lastname[0]}-{self.firstname}{self.lastname}"
            return hash(hash_string)
        else:
            return None


# noinspection DuplicatedCode
class TestDirectorMethods:

    # noinspection DuplicatedCode
    def test_init(self):
        director1 = Director("Taika Waititi")
        director2 = Director("")
        director3 = Director(42)
        director4 = Director("\n")
        director5 = Director("Quo Quo")
        director6 = Director("Taika Woititi")
        director7 = Director("Edgar Allan Poe")
        director8 = Director("Edgar Allan Poe Poe")
        director9 = Director("James Earl Joyce")
        director10 = Director("James earl Joyce")
        director11 = Director("James Earl Jimmy Joyce")
        director12 = Director("James Earl jimmy Jones")
        director13 = Director("Tarantino")
        director14 = Director("James earl Jimmy Jones")
        director15 = Director(".")
        assert repr(director1) == "<Director Taika Waititi>"
        assert director1.lastname == "Waititi"
        assert director2.director_full_name is None
        assert director3.director_full_name is None
        assert director4.director_full_name is None
        assert director1.firstname == "Taika"
        assert director13.lastname == "Tarantino"
        assert director2.__lt__(director4) is None
        assert director7.director_full_name == "Edgar Allan Poe"
        assert director7.firstname == "Edgar"
        assert director7.names_count == 3
        assert director8.names_count == 4
        assert director7.middlenames == "Allan Poe"
        assert director4.__eq__(director4) is True
        assert director4.__eq__(director1) is False
        assert director1.__lt__(director6) is True  # [director1.director_full_name, director6.director_full_name]
        assert director10.__lt__(
            director11) is True  # == [director10.director_full_name, director11.director_full_name]
        assert director11.__lt__(
            director12) is False  # == [director12.director_full_name, director11.director_full_name]
        assert director5.__lt__(director1) is True  # == [director5.director_full_name, director1.director_full_name]
        assert director1.__lt__(director5) is False  # == [director5.director_full_name, director1.director_full_name]
        assert director1.__lt__(director6) is True  # == [director1.director_full_name, director6.director_full_name]
        assert director15.firstname == "."
