# Class Variable
# Problem:Add a class variable to Car that keeps track of the number of cars created

class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        # we can access that type
        # self.total_car += 1 but we acces it like this
        Car.total_car += 1

safariOne = Car("Tata","Safari")

my_car = Car("Tata","Nexon")
# print(my_car.total_car) we can access like this
print(Car.total_car)