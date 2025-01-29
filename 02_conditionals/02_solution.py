age = input("Please enter your age: ")
ageInInt = int(age)

day = input("please enter Day: ")

price = 12 if ageInInt >= 18 else 8

if day == "wednesday":
    # price = price - 2
    price -= 2

print("Ticket price for your movie is $",price)

