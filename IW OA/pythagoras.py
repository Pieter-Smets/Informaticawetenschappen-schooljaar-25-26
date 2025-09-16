import math

zijde_a = int(input("geen de lengte van a in: "))
zijde_b = int(input("geen de lengte van b in: "))

macht_a = math.pow(zijde_a, 2)
macht_b = zijde_b ** 2

som = macht_a + macht_b
zijde_c = math.sqrt(som)
print("De lengte van zijde c is:", zijde_c)