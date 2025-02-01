#Generate a function with yield
# Problem:Write a generator function that yields even number up toa speciefied limit. 

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num)
