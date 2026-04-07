"""
Линейная алгебра
Задание 2
"""

import numpy as np
from sympy import symbols, Eq, solve


x, y, z, v = symbols('x y z v')

A = np.array([[x, 2, 3],
             [-1, y, 4]])

B = np.array([[1, 2, -5],
             [2, -6, z]])

# Умножаю
AAA = 3 * A
BB = 2 * B

# Складываю и получаю левую часть уравнения
AAA_BB = AAA + BB
print(AAA_BB)
"""
[[3*x + 2     10               -1]
 [1        3*y - 12     2*z + 12]]
"""

# Правая часть уравнения
C = np.array([[8, v, -1],
              [1, 6, 4]])

# Система уравнений
eq1 = Eq(AAA_BB[0, 0], C[0, 0])  # 3*x + 2 = 8
eq2 = Eq(AAA_BB[0, 1], C[0, 1])  # 10 = v
eq3 = Eq(AAA_BB[1, 0], C[1, 0])  # -3 + 4 = 1
eq4 = Eq(AAA_BB[1, 1], C[1, 1])  # 3*y - 12 = 6
eq5 = Eq(AAA_BB[1, 2], C[1, 2])  # 2*z + 12 = 4

# Решешие
result = solve((eq1, eq2, eq4, eq5), (x, v, y, z))

print(f"Решение: \n{result}")

"""
Решение: 
{v: 10, x: 2, y: 6, z: -4}
"""
