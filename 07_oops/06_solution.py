# Polymorphism
# Problem: Demostrate polymorphism by definig a method fuel_type in both Car and ElectricCar Classes but with different behaviors.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand}{self.model}"
    
    def fuel_type(self):
        return 'Petrol or Diesel'
        
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return 'Electric Charge'
    

my_tesala = ElectricCar("Tesla","Model S","90kwh")
print(my_tesala.brand)
print(my_tesala.full_name())

print(my_tesala.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())