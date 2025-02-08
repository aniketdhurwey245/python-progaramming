# Inheritance
# Problem:Create an ElectricCar class that inherits from the car class and has an additional attribute battery_size.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        # super() is used to accessing value of parent class
        self.battery_size = battery_size

    

my_tesala = ElectricCar("Tesla","Model S","90kwh")
print(my_tesala.brand)
print(my_tesala.full_name())



