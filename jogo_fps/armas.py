from abc import ABC, abstractmethod, ABCMeta
from golpes import Soco

class Arma(ABC):
    destruicao:float

    def __init__(self,d):
        self.destruicao = d

    def agredir(self,j):
        j.energia -=5

    def __str__(self):
        return f'power {self.destruicao}'

class Faca(Arma):
    lamina:int

    def __init__(self):
        super().__init__(15)
        self.lamina = 10

    def agredir(self,j):
        if self.lamina > 0:
            j.energia -= self.destruicao
            self.lamina -= 1
        else:
            super.agredir(j)

class Soco_ingles(Faca,Soco):
    def agredir(self,j):
        super().agredir(j)
        self.golpear(j)

class Disparavel(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def disparar(self, j):
        pass

    @abstractmethod
    def recarregar(self):
        pass

class Revolver(Arma,Disparavel):
    cartucho : int

    def __init__(self):
        self.cartucho = 6
        self.destruicao = 20

    def disparar(self, j):
        if self.cartucho > 0:
            j.energia -= self.destruicao
            self.cartucho -=1

    def recarregar(self):
        self.cartucho = 6

class Lanca_Chama(Arma,Disparavel):
    gas = float

    def __init__(self):
        self.gas = 100
        self. destruicao = 30

    def disparar(self, j):
        if self.gas > 0:
            j.energia -= self.destruicao
            self.gas -= 5.5

    def recarregar(self):
        self.gas = 100