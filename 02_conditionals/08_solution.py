password = input("Enter password: ")

passLength = len(password)

if passLength < 6:
    strength = "weak"
elif passLength <=10:
    strength = "medium"
else:
    strength = "strong"

print("password stength is:m ",strength)