## dict,{}dictionary declaration work on key value pair

chai_types = {"masala": "spicy", "ginger":"zesty", "green":"mild" }

print(chai_types)

##accesing dictionary

print(chai_types["ginger"])

print(chai_types.get("green"))

##mutation

chai_types["green"] = "Fresh"

print(chai_types)


##loop introduce

for chai in chai_types: ##these method give only key
    print(chai)

for chai in chai_types:
    print(chai, chai_types[chai])

##we can give two variable in loop

for key,value in chai_types.items():

    print(key,value)


## conditional

if "masala" in chai_types:
    print("i have masala chai")


## we can use methods like pop(),  popitem(),del 

del chai_types["green"] 
print(chai_types)

##add items

chai_types["Earl Grey"] = "citrus"
print(chai_types)

##we can alsso make copy using copy method


tea_shop = {
    "chai":{"masala":"spicy", "ginger": "zesty"},
    "tea":{"green":"mild", "black": "strong" }
}

print(tea_shop)

print(tea_shop["chai"]) 

print(tea_shop["chai"]["ginger"])

squared_nums = {x:x**2 for x in range(10)}
print(squared_nums)
squared_nums.clear() ##to empty

print(squared_nums)

##we can take key and value in different dict

keys = ["masala","ginger", "lemon"]
default_value = "delicious"

new_dict = dict.fromkeys(keys,default_value) ##create dictionary use dict key word
print(new_dict)






