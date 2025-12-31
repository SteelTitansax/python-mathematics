""" A al hora de crear el marea Scipy , pensar en como vincular la graficacion de los solvers y esta representacion grafica
    usar libreria de representacion grafica sobre terminal linux , pasar de matplotlib :) 

    Pensar tambien en como crear un graficador funcional 
"""
import plotext as plt
import os 

os.system('clear')

import plotext as plt

# Definir la función
def func(x):
    return 4 * x + 3

# Crear listas de puntos x y y
x_vals = list(range(11))  # Valores de x entre 0 y 10
y_vals = [func(x) for x in x_vals]

# Graficar en la terminal
plt.plot(x_vals, y_vals, label = "line", color = "white")
plt.canvas_color("black")
plt.clear_color()

# Mostrar el gráfico en la terminal
plt.show()
