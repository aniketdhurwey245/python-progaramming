#Debugging Function call
#problem:Create a decorator to print the function name and the values of its arguments every time the function is called.

def function_name(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Calling: {func.__name__} with args {args_value} and kwrgs {kwargs_value}")
        return func(*args,**kwargs)
    return wrapper



@function_name
def greet(name, greeting="Hello"):
    print(f"{greeting},{name}")

greet('Aniket', "Good Morning !")