from abc import ABC,abstractmethod
class Computer:
    def __init__(self):
        self.cpu=None
        self.ram=None
        self.stroage=None


    def __str__(self):
        return f" CPU : {self.cpu},RAM : {self.ram},stroage:{self.stroage}"



class ComputerBuilder(ABC):
        @abstractmethod
        def set_cpu(self,cpu):
            pass

        @abstractmethod
        def set_ram(self,ram):
            pass

        @abstractmethod
        def set_stroage(self,stroage):
            pass
        @abstractmethod
        def get_result(self):
            pass

class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer=Computer()

    def set_cpu(self,cpu):
        self.computer.cpu=cpu
        return self

    def set_ram(self,ram):
        self.computer.ram =ram
        return self

    def set_stroage(self,stroage):
        self.computer.stroage= stroage
        return self

    def get_result(self):
        return self.computer


class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer=Computer()

    def set_cpu(self,cpu):
        self.computer.cpu=cpu
        return self

    def set_ram(self,ram):
        self.computer.ram =ram
        return self

    def set_stroage(self,stroage):
        self.computer.stroage= stroage
        return self

    def get_result(self):
        return self.computer

gaming_computer=(GamingComputerBuilder().set_cpu("intel i9").set_ram("8gb").set_stroage("120gb").get_result())
print(f"gaming_lap:{gaming_computer}")

office_computer=(OfficeComputerBuilder().set_cpu("intel i10").set_ram("12gb").set_stroage("1tb").get_result())
print(f"office_lap:{office_computer}")