# Recursive Function
# Create a recurcive function to calculate the factorial of a number

def facto(n):
    if n == 0:
        return 1
    else:
        return n * facto(n-1)  
    

print(facto(3))
