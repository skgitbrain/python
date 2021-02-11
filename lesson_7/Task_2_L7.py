from abc import ABC, abstractmethod
from datetime import datetime


class Clothes(ABC):

    def __init__(self, param_1):
        self.param_1 = param_1

    @abstractmethod
    def cloth_cons(self):
        pass

    @property
    def timenow(self):
        now = datetime.now()
        return now


class Coat(Clothes):

    def cloth_cons(self):
        return f"Для пальто требуется {self.param_1 / 6.5 + 0.5} ткани"


class Costume(Clothes):

    def cloth_cons(self):
        return f"Для костюма требуется {2 * self.param_1 + 0.3} ткани"


c = Coat(6.5)
print(c.cloth_cons())
co = Costume(1)
print(co.cloth_cons())
print(co.timenow)
