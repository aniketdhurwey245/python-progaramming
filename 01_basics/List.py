tea_varities = ["Black", "Green", "Oolong"]
print(tea_varities)

print(tea_varities[1:3]) ##slicing
 ## list[] is muttable and zero indexing

tea_varities[2] = "Lemon"

print(tea_varities)
for tea in tea_varities :
    print(tea)

tea_varities.append("white") ##append add in last


tea_varities.pop() ## remove last

tea_varities.remove("Green") ## remove anyone you want to remove

tea_varities.insert(1,"green")

tea_varities_copy = tea_varities ## same memory reference

tea_varities_copy = tea_varities.copy() ##different memory reference

squared_nums = [ x**2 for x in range(10)] ##list comprehension

print(squared_nums)

cube_nums = [y**3 for y in range(5)]

print(cube_nums)