number = input("enter number:")

numInInt = int(number)

for i in range(1, 11):
    if i == 5:
        continue
    print(numInInt, 'x', i, '=', numInInt * i)