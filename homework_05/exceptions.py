"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    """Исключение по низкому уровню топлива"""
    pass

class NotEnoughFuel(Exception):
    """Исключение по недостаточности топлива"""
    pass

class CargoOverload(Exception):
    """Исключение по перегрузу"""
    pass
