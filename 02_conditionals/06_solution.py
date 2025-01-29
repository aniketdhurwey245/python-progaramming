distance = input("Give distance of your destination: ")
distanceInInt = int(distance)

if distanceInInt < 3:
    modeOfTransport = "walk"
elif distanceInInt <= 15:
    modeOfTransport ="Bike"
else:
    modeOfTransport = "Car"

print("AI recommends you the transport of: ",modeOfTransport)