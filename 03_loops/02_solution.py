number= input("enter the number :")

num_in_int = int(number)

sum_even = 0
for i in range(1, num_in_int+1):
    if i%2 == 0:
        sum_even +=1

print("sum of even number is :",sum_even )
