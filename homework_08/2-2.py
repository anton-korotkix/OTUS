"""
Матанализ
Задание 2
"""

from sympy import symbols, ln, sqrt, diff
from fractions import Fraction

x1, x2 = symbols('x1 x2')
f = ln(sqrt(x1) + sqrt(x2))

# Производные
df_dx1 = diff(f, x1) # 1/(2*sqrt(x1)*(sqrt(x1) + sqrt(x2)))
df_dx2 = diff(f, x2) # 1/(2*sqrt(x2)*(sqrt(x1) + sqrt(x2)))

# Левая часть
left = x1 * df_dx1 + x2 * df_dx2
left = left.simplify() # 1/2

# Правая часть
right = Fraction(1, 2) # 1/2

print("Левая часть:", left)
print("Правая часть:", right)

if (left == right):
    print("Уравнение выполняется")
else:
    print("Уравнение НЕ выполняется")
