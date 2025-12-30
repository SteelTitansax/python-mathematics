"""NOTE : Please develope these functionalities in Marea STEM"""

# Derivatives 

import sympy 
from sympy import symbols 
import os 

os.system("clear")

x,y = symbols('x y')

# Put the equation here: 

expression = x**3
derivative = sympy.diff(expression,x)
print("derivative:")
print(derivative)

x_value = 2 

answer = derivative.subs(x,x_value)
print("slope at x =", x_value," is ", answer)

# Area under the curve calculation example


dx = 0.1
start_x = 0
end_x = 3
rectangles = int((end_x - start_x)/dx)

sumatory = 0

for diff_a in range(rectangles): 
    x = start_x + dx*diff_a
    y = x**2
    area = y*dx
    sumatory = sumatory + area

print(f"Total area {sumatory}")

# Integral code

x,y,c = symbols('x y c')

eq = x**2
integral = sympy.integrate(eq)
print(f"integral is {integral}")
lower = 0
upper = 3
integral = sympy.integrate(eq,(x,lower,upper))
print(f"the integral with limits is {integral}")
