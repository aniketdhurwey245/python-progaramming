score = input("Give your score:")

scoreInInt = int(score)
if scoreInInt >= 101:
    print("given marks is overflow")
    exit()
    
if scoreInInt >= 90:
    grade = "A"
elif scoreInInt >= 80:
    grade = "B"
elif scoreInInt >= 70:
    grade = "C"
elif scoreInInt >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade is:",grade)