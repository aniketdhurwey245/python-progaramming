# property decorator
# Problem:Use a property decorator in the Car class to make the model attribute read-only
# read only mean there is no change in the value of brand
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.__model = model

    def full_name(self):
        return f"{self.brand} {self.__model}"
    
    @property
    def model(self):
        return self.__model

    
my_car = Car("Tata","Nexon")
# my_car.model = "Safari"   by applying @property decorator 

# print(my_car.model())  we cannot call like this

#call or execute like property

print(my_car.model)