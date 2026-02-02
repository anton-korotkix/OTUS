"""
Создайте класс `Car`, наследник `Vehicle`
"""

from homework_05.base import Vehicle
from homework_05.engine import Engine


class Car(Vehicle):
    """
    Автомобиль
    """
    
    def __init__(self):
        """Инициализатор"""
        self.engine = None #атрибут engine
    
    def set_engine(self, engine: Engine):
        """Установка engine"""
        self.engine = engine
