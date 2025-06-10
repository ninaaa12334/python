class Student:
    def __init__(self, name, age): #konstruktori
        self.__name=name
        self.__age=age
        #deklarimi i metodes get
        @property

        def name(self):
            return self.__name

        #deklarimi i metodes set

        @name.setter
        def name(self,name):
            self.__name=name



        @property
        def name(self):
            return self.__age

        @age.setter
        def name(self, age):
            self.__age = age


student1=Student(name "alice", age:17)

print("Name:", studenti1.name)

student1.name="Bob"
student1.age=18

print("Name:", student1.name)