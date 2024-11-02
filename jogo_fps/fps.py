from typing import List
from armas import Arma, Disparavel
from golpes import Golpe

class Jogador:
    energia: float
    armas : List[Arma]

    def __init__(self):
        self.energia = 150
        self.armas : List[Arma] = []

    def disparar(self,d: Disparavel, j):
        d.disparar(j)

    def municiar(self,d: Disparavel):
        d.recarregar()

    def bater(self, j, g: Golpe= None, a: Arma= None):
        if g == None and a != None:
            a.agredir(j)
        elif a == None and g != None:
            g.golpear(j)

    def __str__(self):
        return f'energia {self.energia}'
