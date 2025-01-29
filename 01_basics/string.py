chai = "Lemon chai"
print(chai)
## string is immutable

chai = "Masala chai"
first_char = chai[0]
print(first_char)
slice_chai = chai[0:6] ##slicing in python
print(slice_chai)
## step size

slice_chai = chai[0:5:2]
print(slice_chai)

## using methods

print(chai.lower())
print(chai.upper())

cofee = "  black cofee  "
print(cofee)
print(cofee.strip()) ## strip method is used to remove extra space

superHeroes = "superman , spiderman ,ironman"
print(superHeroes.replace("spiderman","shaktiman"))
print(superHeroes)

vege = "Lemon, Ginger, Masala, Mint"

##split()method used to convert string into list[]
print(vege.split()) 
print(vege.split(","))
print(vege.find("Masala"))

## order formating format()method

chai_type = "Masala"
quantity = 4
order = "I ordered {} cups of {} chai "
print(order.format(quantity, chai_type))

#convert list to string
chai_variety = ["Lemon", "Masala", "Ginger"]
print(chai_variety)

print(" ".join(chai_variety)) 

