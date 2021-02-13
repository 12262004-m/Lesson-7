from abc import ABC, abstractmethod

class Clothes(ABC):
    itog = 0
    def __init__(self, parametr):
        self.parametr = parametr

    @property
    @abstractmethod
    def consumption(self):
        pass


    def __add__(self, other):
        Clothes.itog +=self.consumption + other.consumption

    def __str__(self):
        return "Итог: "

class Coat(Clothes):
    @property
    def consumption(self):
        return f"Расход ткани на пальто: {round(self.parametr/6.5 + 0.5, 2)}"


class Costume(Clothes):
    @property
    def consumption(self):
        return  f"Расход ткани на костюм: {round(self.parametr*2 + 0.3, 2)}"


l = Coat(40)
m = Costume(60)
print(l+m)