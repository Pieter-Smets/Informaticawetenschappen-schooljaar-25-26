import math

lengte_a = float(input("Geef de lengte van zijde a: "))
lengte_b = float(input("Geef de lengte van zijde b: "))
hoek_alpha = float(input("Geef de grootte van hoek α in graden: "))
hoek_alpha = math.radians(hoek_alpha)

zijde_c = math.sqrt(math.pow(lengte_a,2)+math.pow(lengte_b,2)-(2*lengte_a*lengte_b*math.cos(hoek_alpha)))
print("De lengte van zijde c is: ", zijde_c)