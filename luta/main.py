from luta import *

if __name__ == "__main__":
    popo = Boxeador("Popo")
    bambam = Boxeador("Bambam")
    wind = Boxeador("Whindersson")
    connor = MMA("Mc Gregor")
    chapolin = Jujitsu("Chapolin Colorado")

    popo.soco(bambam)

    print("\nPopó deu um murro do Bambam!!")
    print(popo)
    print(bambam)

    print("\nPopó deu um gancho de direita do Bambam!!")
    popo.gancho(bambam)
    print(popo)
    print(bambam)

    print("\nWHINDERSSON NUNES APARECE!!")
    print("\nWhinderson Nunes deu um soco no Popó, salvando o Bambam")
    wind.gancho(popo)
    print(popo)
    print(bambam)

    print("\nPopó se vê numa fria 2 x 1, pode isso????")
    print("\nPopó chama o mano Connor McGregor pra dar uma surra em todo mundo")
    print("\nMcGregor chega quebrando no Whindersson, metendo um SUPERMAN PUNCH!!!!!!!")
    connor.superman_punch(wind)
    print(wind)

    print("\nWhindersson grita: E agora, quem poderá nos defender?")

    print("\nEle: o Chapolin Colorado! Não contavam com a minha astúcia")

    print("\nChapolin chega chegando em McGregor, derruba-o e dá uma chave de braço que apaga o lutador!!!")

    chapolin.chave_braco(connor)
    print(connor)

    print("\nKO!!!!")

    print("\nTHE FIGHT IS OVER")



