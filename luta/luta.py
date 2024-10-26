from abc import ABC


class Lutador(ABC):
    nome: str
    energia: float

    def __init__(self, n: str):
        self.nome = n
        self.energia = 100

    def __str__(self):
        return f'Nome: {self.nome}, energia: {self.energia} %'

    def soco(self, oponente):
        oponente.energia -= 5.5


class Boxeador(Lutador):
    def cruzado(self, oponente):
        oponente.energia -= 10.2

    def gancho(self, oponente):
        oponente.energia -= 20.8


class Muay_Thai(Boxeador):
    def chute_alto(self, oponente):
        oponente.energia -= 15.4


class Jujitsu(Lutador):
    def chave_braco(self, oponente):
        oponente.energia -= 100


class MMA(Muay_Thai, Jujitsu):
    def superman_punch(self, oponente):
        oponente.energia -= 53.2
