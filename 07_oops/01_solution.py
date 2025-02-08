# Basic Class and Object 
# Problem:Create a Car class with attributes like brand and model.Then create an instance of this class.
#declaration of class
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
#here init is constructor


my_car = Car('Toyota','Corolla')#creation object
print(my_car.brand)#accessing the values
print(my_car.model)

my_new_car = Car("tata","Safari")
print(my_new_car.brand)
print(my_new_car.model)