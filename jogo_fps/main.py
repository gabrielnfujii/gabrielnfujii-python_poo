from fps import Jogador
from armas import Lanca_Chama, Revolver
from golpes import Soco

if __name__ == "__main__":

    j1 = Jogador()
    j2 = Jogador()
    print(j1)
    print(j2)

    lc1 = Lanca_Chama()

    j1.armas.append(lc1)
    j2.armas.append(Revolver())

    j1.armas[0].disparar(j2)
    j2.armas[0].disparar(j1)

    print(j1)
    print(j2)

    j1.bater(j2,Soco())
    j1.bater(j2, a= j1.armas[0])
    print(j1)
    print(j2)