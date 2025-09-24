import copy
from abc import ABC, abstractmethod

class Car:
    def __init__(self):
        self.wheels = None
        self.hp = None
        self.seat = None
        self.color = None
        self.fuel_type = None

    def __str__(self):
        return f'Wheels:{self.wheels}  HP:{self.hp}  Seat:{self.seat} Color:{self.color} Fuel_Type:{self.fuel_type}'

    # def clone(self):
    #     return copy.deepcopy(self)





class CarBuilder(ABC):
    @abstractmethod
    def build_wheel(self, wheels):
        pass

    @abstractmethod
    def build_hp(self, hp):
        pass

    @abstractmethod
    def build_seat(self, seat):
        pass

    @abstractmethod
    def build_fuel(self, fuel_type):
        pass

    @abstractmethod
    def get_car(self):
        pass


class FamilyCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def build_wheel(self, wheels):
        self.car.wheels = wheels
        return self

    def build_seat(self, seat):
        self.car.seat = seat
        return self

    def build_hp(self, hp):
        self.car.hp = hp
        return self

    def build_fuel(self, fuel_type):
        self.car.fuel_type = fuel_type
        return self

    def get_car(self):
        return self.car


class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def build_wheel(self, wheels):
        self.car.wheels = wheels
        return self

    def build_seat(self, seat):
        self.car.seat = seat
        return self

    def build_hp(self, hp):
        self.car.hp = hp
        return self

    def build_fuel(self, fuel_type):
        self.car.fuel_type = fuel_type
        return self

    def get_car(self):
        return self.car


# chain of resposnibilities
family_car = (FamilyCarBuilder().build_wheel("steel wheels").build_seat("4").build_hp("320 CC").build_fuel("6L").get_car())
print(family_car)