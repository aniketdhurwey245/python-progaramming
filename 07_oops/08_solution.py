# static Method
# Problem:Add a static method to the Car class that return a general description of a car.
# staic method having access to the class but not to the object of the class that is called static methode

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    @staticmethod # that is call decorater and we are define static method
    def general_description():
        # A static method does not need to access instance-specific data key self
        return "Car are means of transport"
    

    def full_name(self):
        return f"{self.brand} {self.model}"
    
#creating an object
my_car = Car("Toyota","Corolla")

#Accesing the static method using class it is technicaly recomended
print(Car.general_description())


# It's allowed but not recommended to access static methods via the object
# Technically works, but not recommended
print(my_car.general_description())

print(my_car.full_name())