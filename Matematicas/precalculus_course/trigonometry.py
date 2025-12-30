import math 
import os 

os.system("clear")

cateto_contiguo = 2
cateto_opuesto = 3
hipotenusa = 5

seno = cateto_opuesto / hipotenusa 
coseno = cateto_contiguo / hipotenusa
tangente = cateto_opuesto / cateto_contiguo 

print(f"Cateto opuesto : {cateto_opuesto}")
print(f"Cateto contiguo : {cateto_contiguo}")
print(f"Hipotenusa : {hipotenusa}")

print(f"Seno : {seno}")
print(f"Coseno : {coseno}")
print(f"Tangente : {tangente}")

seno = math.sin(4/5)
coseno = math.cos(5/6)
tangente = math.tan(7/9)

print(f"seno con math {seno}")
print(f"coseno con math {coseno}")
print(f"tangente con math {tangente}")

print(f"angulo de seno {math.degrees(seno)}")

