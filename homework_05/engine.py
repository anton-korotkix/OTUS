"""
Создайте dataclass `Engine`
"""

from dataclasses import dataclass


@dataclass
class Engine:
    """Двигатель"""
    volume: float = 1.6 #атрибут объема
    pistons: int = 4 #атрибут количества цилиндров
