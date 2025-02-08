username = 'aniket' #global scope it is access in anywhere of code 

def func():
    username = 'Dhurwey'
    print(username)#this only used in the scope of function

print(username)

func()
x=99
def f1():
    x = 88
    def f2():
        print(x)
    return f2

myResult = f1()#here my result having whole def of f2

myResult()

def closure(num):
    def actual(x):
        return x**num
    return actual

f = closure(2)
g = closure(3)

print(f(3))
print(g(3))#closure or bag pack
