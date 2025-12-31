""" ME quede en el minuto 7:30:00 """

""" Mirar como implementarlo en Marea STEM """
import plotext as plt
import os 
import numpy as np
from sympy import *

os.system('clear')

xmin = -10
xmax = 10
ymin = -10
ymax = 10


#Define how many points to plot

points = xmax-xmin

#Define the array of x values once 

x = np.linspace(xmin,xmax,points)

y1 = 2*x

y2 = (x**2) - 3 

# Graphic in terminal line 1 
plt.plot(x,y1, label="Ecuation 1", color = "blue")
plt.title('Linear ecuation example')


# Graphic in terminal line 1 
plt.plot(x,y2, label="Ecuation 2", color = "red")
plt.title('Linear ecuation example')

plt.canvas_color("black")

plt.clear_color()
plt.grid(-10,10)       # to add vertical grid lines

# Mostrar el gráfico en la terminal
plt.show()

print('Solving the equations system')
x,y = symbols('x y')
first = 2*x + y - 1
second = x - 2*y + 7 

print(linsolve([first,second],(x,y)))
