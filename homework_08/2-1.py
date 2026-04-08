"""
Матанализ
Задание 1
"""

import sympy as sp

x1, x2 = sp.symbols('x1 x2')

f = x1**3 - 2*x1*x2 + x2**2 - 3*x1 - 2*x2

# Вычисляю градиент
grad_f = [sp.diff(f, x1), sp.diff(f, x2)]
print(f"Градиент функции: \n{grad_f}")
"""
Градиент функции:
[3*x1**2 - 2*x2 - 3, -2*x1 + 2*x2 - 2]
"""

# Производные
df_dx1 = sp.diff(f, x1) # 3*x1**2 - 2*x2 - 3
df_dx2 = sp.diff(f, x2) # -2*x1 + 2*x2 - 2

# Критические точки через систему уравнений
critical_points = sp.solve([df_dx1, df_dx2], (x1, x2))
print(f"Критические точки: \n{critical_points}")

"""
Критические точки: 
[(-1, 0), (5/3, 8/3)]
"""
