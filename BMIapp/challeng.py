from abc import ABC


class ClassName(ABC):  # this is the final definition of an abstract class ABC is important

    pass


class Person(ABC):
    def __init__(self, name, age, weight, height):  # konstruktori
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

        @property
        def name(self,name):
            return self.__name


        @name.setter
        def name(self, age):
            self.__age = age

        @property
        def name(self, weight):
            return self.__weight

        @age.setter
        def name(self, height):
            self.__height = height










        class Adult:
            def __init__(self,name, age, weight, height):
                self.__name = name
                self.__age = age
                self.__weight = weight
                self.__height = height

                @property
                def name(self):
                    return self.__name

                @name.setter
                def name(self, age):
                    self.__age = age

                @property
                def name(self):
                    return self.__weight

                @age.setter
                def name(self, age):
                    self.__age = height

                def area(self):
                    return 3.14 * self.radius * self.radius


class Child:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, age):
        self.__age = age

    @property
    def name(self):
        return self.__weight

    @age.setter
    def name(self, age):
        self.__age = height


            def area(self):
                     return self.weight / self.height



  class MBIapp:

