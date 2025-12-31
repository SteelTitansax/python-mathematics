import math
import os
""" Sacar funcionalidad para marea scipy de esto pudiendo desde graficar hasta sacar punto deseado  """

os.system('clear')


# Coefficient values

a = 1 
b = 5
c = 6

print("y = ",a,"x**2 + ",b,"x + ",c)

vx = -b/(2*a)
vy = a*(vx**2) + b*vx + c

print("Vertex: (",vx,",",vy,")")

# Roots

d = b**2 - 4*a*c
if d>=0: 
    root_1 = (-b + math.sqrt(d))/(2*a)
    root_2 = (-b - math.sqrt(d))/(2*a)
    print("Roots: x = ", root_1, " and x = ", root_2)
else:
    print("No real roots")

