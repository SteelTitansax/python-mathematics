import sympy 
from sympy.solvers import solve
from sympy import symbols
import os

"""Pensar en como poner esto de manera que puedas introducir una ecuacion o conjunto de ecuaciones y hacer solvers y graficar """

os.system('clear')

x = symbols('x')

# Put your ecuation here
# ------------------------------
eq = x**2 - 4
#eq = input('Enter equation 0 = ')
print("x = ", solve(eq,x))


from sympy import *
# Resolution for x,y variables 
# ------------------------------
y = symbols('y')

var('x y')

# First equation set equal to zero, ready to solve

first = 2*x + 10 

# Sympy syntax for equation equal to zera, ready to factor 

eq1 = Eq(first, y)

# Sympy solve for x 

sol = solve(eq1,x)

# Show factored results

print("x = ", sol[0])

""" Esto es otra funcionalidad del chatbot, pidele que factorize """
# Equation set equal to zero , ready to solve

eq = 2*x + 10*y + 4

# eq = x**3 - 2*x**2 - 5*x + 6

factorization = sympy.factor(eq)

print(factorization)