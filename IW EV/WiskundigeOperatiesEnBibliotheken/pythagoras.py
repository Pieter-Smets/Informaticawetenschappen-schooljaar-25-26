import math

zijde_a = float(input("Geef de lengte van zijde a: "))
zijde_b = float(input("Geef de lengte van zijde b: "))

macht_zijde_a = math.pow(zijde_a, 2)
macht_zijde_b = math.pow(zijde_b, 2)

macht_zijde_c = macht_zijde_a + macht_zijde_b
zijde_c = math.sqrt(macht_zijde_c)


print("De lengte van zijde c is: ", zijde_c)

