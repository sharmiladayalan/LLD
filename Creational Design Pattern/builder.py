from abc import ABC ,abstractmethod

#Product

class Computer:
    def __init__(self):
        self.cpu=None
        self.ram=None
        self.storage=None
        
    def __str__(self):
        return f"CPU: {self.cpu},RAM : {self.ram} , storage: {self.storage}"
    
    
#Builder Interface

class ComputerBuilder(ABC):
    
    @abstractmethod
    def set_cpu(self):
        pass
    
    @abstractmethod
    def set_ram(self):
        pass
    
    @abstractmethod
    def set_storage(self):
        pass
    
    @abstractmethod
    def get_result(self):
        pass
    
#Concrete builder

class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer=Computer()
        
    def set_cpu(self):
        self.computer.cpu="Intel i9"
        
    def set_ram(self):
        self.computer.ram="32GB"
        
    def set_storage(self):
        self.computer.storage="1TB SSD"
        
    def get_result(self):
        return self.computer
    
class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer=Computer()
        
    def set_cpu(self):
        self.computer.cpu="Intel i5"
        
    def set_ram(self):
        self.computer.ram="16GB"
        
    def set_storage(self):
        self.computer.storage="228 SSD"
        
    def get_result(self):
        return self.computer
    
#Director

class Director:
    def __init__(self,builder :ComputerBuilder):
        self.builder: ComputerBuilder=builder
        
    def construct_computer(self):
        self.builder.set_cpu()
        self.builder.set_ram()
        self.builder.set_storage()
        return self.builder.get_result()
    
#Client code

gaming_builder=GamingComputerBuilder()
director=Director(gaming_builder)
gaming_pc=director.construct_computer()
print(gaming_pc)

office_builder=OfficeComputerBuilder()
director=Director(office_builder)
office_pc=director.construct_computer()
print(office_pc)
    