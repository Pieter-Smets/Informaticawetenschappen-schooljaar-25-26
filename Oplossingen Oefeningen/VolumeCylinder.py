import math


hoogte = int(input("geef de hoogte in: "))
diameter = int(input("geef de diameter in: "))

volume = 1/4*math.pi*math.pow(diameter,2)*hoogte
print ("het volume is: ", volume)