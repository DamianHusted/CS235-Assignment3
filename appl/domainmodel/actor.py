# noinspection DuplicatedCode,SpellCheckingInspection
class Actor:
    __actor_full_name: str
    __actor_id: int

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str or actor_full_name == "\n":
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
            self.colleague_dict = {f"{self.__repr__()}": []}
            #   check for multiple names
            self.names_count = self.__actor_full_name.count(" ") + 1
            #   assign first and last names
            if self.names_count < 3:
                if " " in self.__actor_full_name:
                    self.firstname = self.actor_full_name[:self.__actor_full_name.find(" ")]
                    self.lastname = self.actor_full_name[self.__actor_full_name.find(" ") + 1:]
                else:
                    self.firstname = self.__actor_full_name
                    self.lastname = self.actor_full_name  # In case actor goes by single name, first and last name
                    # will be assigned the same name for indexing purposes.
            #   Assign first, middle and last names
            else:
                self.firstname = self.actor_full_name[:self.__actor_full_name.find(" ")]
                self.middlenames = self.__actor_full_name[
                                   actor_full_name.find(" ") + 1: self.__actor_full_name.rfind("")]
                self.lastname = self.__actor_full_name[self.__actor_full_name.rfind(" ") + 1:]
            self.__firstname = self.firstname
            self.__lastname = self.lastname
            self.__actor_id = self.__hash__()


    def check_if_this_actor_worked_with(self, colleague):
        if colleague.actor_full_name in self.colleague_dict[self.__repr__()]:
            return True
        elif self.actor_full_name in colleague.colleague_dict[colleague.__repr__()]:
            return True
        else:
            return False

    def add_actor_colleague(self, colleague):
        if colleague.actor_full_name not in self.colleague_dict.values():
            self.colleague_dict[self.__repr__()].append(colleague.actor_full_name)

        if self.actor_full_name not in colleague.colleague_dict.values():
            colleague.colleague_dict[colleague.__repr__()].append(self.actor_full_name)

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        return self.__actor_full_name == other.__actor_full_name

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
            hash_string = f"{self.firstname[0]}{self.lastname}-{self.firstname}{self.lastname}-{self.__actor_full_name}"
            return hash(hash_string)
        else:
            return None
    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        self.__lastname = value

    @firstname.setter
    def firstname(self, value):
        self.__firstname = value


# noinspection DuplicatedCode
class TestActorMethods:

    def test_init(self):
        actor1 = Actor("Taika Waititi")
        actor2 = Actor("")
        actor3 = Actor(42)
        actor4 = Actor("\n")
        actor5 = Actor("Quo Quo")
        actor6 = Actor("Taika Woititi")
        actor7 = Actor("Edgar Allan Poe")
        actor8 = Actor("Edgar Allan Poe Poe")
        actor9 = Actor("James Earl Joyce")
        actor10 = Actor("James earl Joyce")
        actor11 = Actor("James Earl Jimmy Joyce")
        actor12 = Actor("James Earl jimmy Jones")
        actor13 = Actor("Tarantino")
        actor14 = Actor("James earl Jimmy Jones")
        actor15 = Actor(".")
        assert repr(actor1) == "<Actor Taika Waititi>"
        assert actor1.lastname == "Waititi"
        assert actor2.actor_full_name is None
        assert actor3.actor_full_name is None
        assert actor4.actor_full_name is None
        assert actor1.firstname == "Taika"
        assert actor13.lastname == "Tarantino"
        assert actor14.__lt__(actor12) == "Possible duplicate"
        assert actor2.__lt__(actor4) is None
        assert actor7.actor_full_name == "Edgar Allan Poe"
        assert actor7.firstname == "Edgar"
        assert actor7.names_count == 3
        assert actor8.names_count == 4
        assert actor7.middlenames == "Allan Poe"
        assert actor4.__eq__(actor4) is True
        assert actor4.__eq__(actor1) is False
        assert actor1.__lt__(actor6) is True  # [actor1.actor_full_name, actor6.actor_full_name]
        assert actor9.__lt__(actor10) == "Possible duplicate"
        assert actor10.__lt__(actor11) is True  # == [actor10.actor_full_name, actor11.actor_full_name]
        assert actor11.__lt__(actor12) is False  # == [actor12.actor_full_name, actor11.actor_full_name]
        assert actor5.__lt__(actor1) is True  # == [actor5.actor_full_name, actor1.actor_full_name]
        assert actor1.__lt__(actor5) is False  # == [actor5.actor_full_name, actor1.actor_full_name]
        assert actor1.__lt__(actor6) is True  # == [actor1.actor_full_name, actor6.actor_full_name]
        assert actor15.firstname == "."

# actor1 = Actor("Taika Waititi")
# actor2 = Actor("")
# actor3 = Actor(42)
# actor4 = Actor("\n")
# actor5 = Actor("Quo Quo")
# actor6 = Actor("Taika Woititi")
# actor7 = Actor("Edgar Allan Poe")
# actor8 = Actor("Edgar Allan Poe Poe")
# actor9 = Actor("James Earl Joyce")
# actor10 = Actor("James earl Joyce")
# actor11 = Actor("James Earl Jimmy Joyce")
# actor12 = Actor("James Earl jimmy Jones")
# actor13 = Actor("Tarantino")
# actor14 = Actor("James earl Jimmy Jones")
# actor15 = Actor(".")
#
# print(actor1.__hash__())
# print(actor2.__hash__())


# actor1 = Actor("Cameron Diaz")
# actor2 = Actor("Angelina Jolie")
# actor3 = Actor("Brad Pitt")
# print(actor1 < actor2)
# print(actor1 > actor3)
# print(actor2 < actor3)

# actor1 = Actor("Angelina Jolie")
# print(actor1)
# actor2 = Actor("")
# print(actor2)
# actor3 = Actor(42)
# print(actor3)
# actor4 = Actor("Brad Pitt")
# actor5 = Actor("Seth Rogan")
# print(actor1.check_if_this_actor_worked_with(actor4))
# print(actor1.add_actor_colleague(actor4))
# print(actor1.add_actor_colleague(actor5))
# print(actor1.check_if_this_actor_worked_with(actor4))
# print(actor4.check_if_this_actor_worked_with(actor1))
# print(actor1.check_if_this_actor_worked_with(actor5))
#
