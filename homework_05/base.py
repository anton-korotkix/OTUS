"""
Доработайте класс `Vehicle`
"""

from abc import ABC
from homework_05 import exceptions


class Vehicle(ABC):
    """
    Базовый класс
    """
    
    def __init__(self, weight: float = 100.0, fuel: float = 50.0, fuel_consumption: float = 7.0, started: bool = False):
        """Инициализатор"""
        self.weight = weight #атрибут веса
        self.fuel = fuel #атрибут топлива
        self.fuel_consumption = fuel_consumption #атрибут расхода
        self.started = started #атрибут состояния
    
    def start(self):
        """Запуск"""
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
              raise LowFuelError("Нет топлива")
    
    def move(self, distance):
        """Движение"""        
        if self.fuel >= (distance / self.fuel_consumption):
            self.fuel = self.fuel - (distance / self.fuel_consumption)
        else:
            raise NotEnoughFuel("Недостаточно топлива")
