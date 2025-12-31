import plotext as plt
import os 
import numpy as np

""" Sacar funcionalidad para marea scipy de esto pudiendo desde graficar hasta sacar punto deseado  """

os.system('clear')

x1 = 1
y1 = 7
x2 = 2
y2 = 10

# The vector is "m"

m = (y2-y1) / (x2-x1)

# The y intercept is "b"

b = y1 - m*x1

x_vals = np.linspace(x1,x2,10)
y_vals = m*x_vals + b

# Graficar en la terminal
plt.plot(x_vals, y_vals , label="linear ecuation xy", color = "white")
plt.title('Linear ecuation example')
plt.xlabel('x')
plt.ylabel('y')
plt.canvas_color("black")
plt.clear_color()

# Mostrar el gráfico en la terminal
plt.show()

 