import math

massa = int(input("Geef de massa in kg: "))
snelheid = int(input("Geef de snelheid in m/s: "))
kinetische_energie = massa * math.pow(snelheid, 2) / 2
print("De kinetische energie is: ", kinetische_energie, "Joule")