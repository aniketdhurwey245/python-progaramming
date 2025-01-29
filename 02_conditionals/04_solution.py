color = input("Enter fruits color:")

if color == "Green":
    fruits = "Unripe"

elif color == "Yellow":
    fruits = "Ripe"

elif color == "Brown":
    fruits = "Overripe"
else:
    print("Please enter a valid color")

print("we determined condition of fruits on the basis of color: ",fruits)
    
# another methods to question

fruitName = input("Give fruits name:")
fruitColor = input("fruit color is:")

if fruitName == "Mango":
    if fruitColor == "Green":
        print("fruit is UnRipe")
    elif fruitColor == "Yellow":
        print("fruit is Ripe")
    elif fruitColor == "Brown":
        print("fruit is OverRipe")
    else:
        print("Please give a valid color")


if fruitName == "Banana":
    if fruitColor == "Green":
        print("fruit is UnRipe")
    elif fruitColor == "Yellow":
        print("fruit is Ripe")
    elif fruitColor == "Brown":
        print("fruit is OverRipe")
    else:
        print("Please give a valid color")