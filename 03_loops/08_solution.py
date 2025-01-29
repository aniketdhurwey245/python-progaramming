input_char = input("give input character :")



for char in input_char:
    if input_char.count(char)==1:
        print("Char is :", char)
        break

# for all non repeated char

for char in input_char:
    if input_char.count(char)==1:
        print("Char is :", char)
        