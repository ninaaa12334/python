from abc import ABC

class ClassName(ABC): #this is the final definition of an abstract class ABC is important

    pass

class Shape(ABC): #klasa abstrakte
    #metode abstrakte
    @abstractmethod
    def area(self):
        pass

    class Circle(Shape):
        def __init__(self, radius):
            self.radius=radius

            def area(self):
                return 3.14*self.radius*self.radius

            class Square(Shape):
                def __init__(self, length):
                    self.length = length

                    def area(self):
                        return self.length * self.length

#objektet per keto dy klasa
circle_1=Circle(7)
square_1=Square(18)

print(circle_1.area())
print(square_1.area())

#klasat abstrakte mund te kene edhe metoda te thjeshta edhe abstrakte
#interfejsat jane klasa abstrakte qe kane vetem metoda abstrakte

