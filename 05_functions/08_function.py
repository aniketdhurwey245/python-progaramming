# Function with **kwargs
# Problem:create a function that accepts any number of keyword arguments and prints them in the format key:value

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Ironman", power="Lazer")
print_kwargs(name="Ironman")
print_kwargs(name="Ironman", power="Lazer", enemy="DR.Jackaal")        
