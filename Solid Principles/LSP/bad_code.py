


"""
    ==> This module demonstrates a violation of the Liskov Substitution Principle (LSP).

    ==> Ojects of a superclass should be replaceable with objects of its
        subclasses without affecting the correctness of the program.

    ==> If a class B is a subclass of class A, then B should be usable anywhere A is expected,
        without surprises.

    ==> Substitutability,?
        => Not just having the same methods, but ensuring they work consistently with what
            clients expect from the base class.
"""

""""
    2. why its matter.?
        => prevents inheritance issues.
        => helps polymorphism. woks safely.
        => Avoid "is - a" relationship that break logic (classic square - rectangle problem).
"""

"""Bad Example:
    => Here, the Square class inherits from Rectangle, but it overrides the set_width and
        set_height methods in a way that violates the expectations set by the Rectangle class.
    
    => This can lead to unexpected behavior when a Square is used in place of a Rectangle."""


"""Bad code example:"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height
    

class Square(Rectangle):
    def set_width(self, w: int):
        self.width = w
        self.height = w

    def set_height(self, h: int):
        self.height = h
        self.width = h

    def print_area(rect: Rectangle):
        rect.set_width(5)
        rect.set_height(10)
        print(f"Area: {rect.area()}")

rectangle = Rectangle(5,4)
print(rectangle.area())

square = Square(10,4)
print(square.area())

#Problem...
# 
# A square is not a rectangle in terms of behavior.
# When we set the width and height of a square, they must always be equal.
# 
# client code breaks expectation voilates LSP        