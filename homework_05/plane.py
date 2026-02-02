"""
Создайте класс `Plane`, наследник `Vehicle`
"""

from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload


class Plane(Vehicle):
    """
    Самолет
    """
    
    def __init__(self, weight: float = 100.0, fuel: float = 50.0, fuel_consumption: float = 7.0, cargo: float = 0.0, max_cargo: float = 100.0):
        """Инициализатор"""
        self.cargo = cargo #атрибут текущего груза
        self.max_cargo = max_cargo #атрибут максимального лимита груза
        
    def load_cargo(self, cargoAdd):
        """Принимает число cargoAdd, проверяет, что в сумме с текущим cargo не будет перегруза"""
        if self.max_cargo >= (self.cargo + cargoAdd):
            self.cargo = (self.cargo + cargoAdd)
        else:
            raise CargoOverload("Перегруз")
            
    def remove_all_cargo(self) -> float:
        """Обнуляет значение cargo и возвращает значение cargo, которое было до обнуления"""
        cargo = self.cargo
        self.cargo = 0.0
        return cargo
