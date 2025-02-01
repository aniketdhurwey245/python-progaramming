# function with *args
# Problem:Write a function that takes variable number of arguement and returns their sum.

def sum_all(*args):
    return sum(args)

print(sum_all(3,4))
print(sum_all(3,4,1))
print(sum_all(3,4,6,9))
print(sum_all(3,4,1,2,7,))

# args ke jagah kuchh bhi likh sakhte ho * ka hona jaruri h
