

"""
    ==> Instead of forcing inheritance, extract a commaon abstraction (shape) and implement properly.
"""

"""Good Example:
    => Here, both Rectangle and Square implement the Shape interface, ensuring they adhere to
    => This way, they can be used interchangeably without violating LSP."""
"""
Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program.
    => the same contract defined by the Shape interface.
"""

"""Good code example:"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def set_side(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
rectangle = Rectangle(5, 10)
print(f"Rectangle area: {rectangle.area()}") 

square = Square(5)
print(f"Square area: {square.area()}")
