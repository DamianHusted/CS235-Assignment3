from appl.domainmodel.movie import Movie
from datetime import *


class Watchlist:
    __watchlist: list
    __size: int
    __watchlist_id: int
    __change_history: dict
    __past_watchlists: dict

    def __init__(self):
        self.__watchlist = []
        self.__size = len(self.__watchlist)
        self.__watchlist_id = id(self)
        self.__change_history = {"Additions": [], "Deletions": [], "Resets": []}
        self.__past_watchlists = {}

    @property
    def watchlist(self):
        return self.__watchlist

    @watchlist.setter
    def watchlist(self, new_watchlist):
        if isinstance(new_watchlist, Watchlist):
            if self.__watchlist is not None or len(self.__watchlist) == 0:
                change_time = datetime.now().strftime("%d/%m%/Y at %H:%M:%S")

                self.__change_history["Resets"].append(change_time, self.__watchlist_id)
                self.__past_watchlists[change_time] = (self.__watchlist, self.__watchlist_id, self.__size)

            self.__watchlist = new_watchlist

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        self.__size = new_size

    @property
    def watchlist_id(self):
        return self.watchlist_id

    @property
    def change_history(self):
        return self.__change_history

    @property
    def past_watchlists(self):
        return self.__past_watchlists

    @property
    def __repr__(self):
        return f"<Watchlist {self.__watchlist_id}>"

    def __eq__(self, other):
        if self.__size == other.__size:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__size < other.__size:
            return True
        else:
            return False

    def __hash__(self):
        hash_string = ""
        if self.__size > 0:
            hash_string += [str(item) for item in sorted(self.__watchlist)]
        else:
            hash_string = str(self.__watchlist_id)
        return hash(hash_string + str(self.__size))

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.__size - 1:
            self.index += 1
            return self.__watchlist[self.index]
        else:
            raise StopIteration

    def add_movie(self, movie_to_add: Movie):
        add_time = datetime.now().strftime("%d/%m%/Y at %H:%M:%S")
        if self.__watchlist is None or movie_to_add not in self.__watchlist or len(self.__watchlist) == 0:
            if isinstance(movie_to_add, Movie):
                # noinspection PyUnresolvedReferences
                self.__watchlist.append(movie_to_add)
                self.__size += 1
                self.__change_history["Additions"].append((movie_to_add.title, add_time))
                # print(f"Movie {movie_to_add.title} is added to your watchlist!")
            else:
                pass
        else:
            pass

    def remove_movie(self, movie_to_remove: Movie):
        if self.__watchlist is None or movie_to_remove not in self.__watchlist or len(self.__watchlist) == 0:
            pass
        else:
            self.__watchlist.remove(movie_to_remove)
            self.__size -= 1
            while True:
                user_confirm_removal = input(f"Are you sure you want to remove {movie_to_remove.title} "
                                             f"from your watchlist? \nEnter Y to confirm and N to decline: ")
                if user_confirm_removal.lower() == "y":
                    self.__watchlist.remove(movie_to_remove)
                    self.__size -= 1
                    # print(f"{movie_to_remove.title} is removed from your watchlist")
                    break
                elif user_confirm_removal.lower() == "n":
                    break

    def first_movie_in_watchlist(self):
        if self.__watchlist is None or len(self.__watchlist) == 0:
            pass
        else:
            return self.__watchlist[0]

    def select_movie_to_watch(self, movie_index):
        try:
            return self.__watchlist[movie_index]
        except IndexError:
            return None

    def size(self):
        return len(self.__watchlist)


# watchlist = Watchlist()
# print(f"Size of watchlist: {watchlist.size()}")
# watchlist.add_movie(Movie("Moana", 2016))
# watchlist.add_movie(Movie("Ice Age", 2002))
# watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
# print(watchlist.first_movie_in_watchlist())

# watchlist1 = Watchlist()
# watchlist1.add_movie(Movie("Xanax diaries", 2016))
# watchlist1.add_movie(Movie("Molly's party", 2002))
# watchlist1.add_movie(Movie("Guardians of the Ganja", 2012))
# print(f"Size of watchlist: {watchlist1.size()}")
# watchlist1.remove_movie(Movie("James Bond", 1998))
# watchlist1.add_movie(Movie("You me and Dupree", 1900))
# watchlist1.add_movie(Movie("Mad Max", 1989))
# print(watchlist1.first_movie_in_watchlist())
# print(watchlist1.select_movie_to_watch(3))

# watchlist2 = Watchlist()
# print(f"Size of watchlist: {watchlist2.size()}")
# watchlist2.add_movie(Movie("James Bond", 1998))
# watchlist2.add_movie(Movie("James Bond", 1998))
# print(f"Size of watchlist: {watchlist2.size()}")
# print(watchlist2.first_movie_in_watchlist())
#
# watchlist3 = Watchlist()
# watchlist3.add_movie(Movie("James Bond", 1998))
# print(watchlist3.first_movie_in_watchlist())
# print(watchlist3.select_movie_to_watch(20))

# #
# watchlist4 = Watchlist()
# watchlist4.add_movie(Movie("You me and Dupree", 1900))
# print(watchlist4.first_movie_in_watchlist())
# watchlist4.add_movie(Movie("Mad Max", 1989))
# watchlist4.add_movie(Movie("Snatch", 2001))
# watchlist4.add_movie(Movie("The Mask", 1996))
# print(watchlist4.size())
# watchlist4.remove_movie(Movie("Snatch", 2001))
# print(watchlist4.size())
# watchlist4.remove_movie(Movie("Snatch", 2001))
# print(watchlist4.size())

#
#
# # print(watchlist4.watchlist[2])
# # print(sorted(watchlist4.watchlist))
#
#
#
# watchlist5 = Watchlist(12)
# print(watchlist5.watchlist)
#
# for item in watchlist4:
#     print(item)
