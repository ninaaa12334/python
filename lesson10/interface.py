from abc import ABC,

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass

class Book(Printable):
    def__init__(self,title, author):
    self.title=title
    self.author=author

    def print_info(self):
        print(f"Book:{self.title} by {self.author}")

libri=Book(title: "Hija e maleve", author: "Isnail Kadare")




class DigitalSchool:
    def __init__(self, name, city, state):
        self.__name=name
        self.__city=city
        self.__state = state
        #deklarimi i metodes get
        @property

        def name(self):
            return self.__name

            # deklarimi i metodes set

        @name.setter
        def name(self, name):
            self.__name = name

