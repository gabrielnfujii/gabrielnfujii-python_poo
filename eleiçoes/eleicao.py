import csv
import pickle
from typing import List
from datetime import date
from Interface_Eleicao import Transparencia
from commom import *
class Urna(Transparencia):
    mesario : Pessoa
    __secao : int
    __zona : int
    __eleitores_presentes : List[Eleitor] = []
    __votos = {}  # dicionario chave = numero do candidato, valor é a quantidade de votos

    def __init__(self, mesario: Pessoa, secao: int, zona: int,
                 candidatos: List[Candidato], eleitores: List[Eleitor]):
        self.mesario = mesario
        self.__secao = secao
        self.__zona = zona
        self.__nome_arquivo = f'{self.__zona}_{self.__secao}.pkl'
        self.__candidatos = candidatos
        self.__eleitores = []
        for eleitor in eleitores:
            if eleitor.zona == zona and eleitor.secao == secao:
                self.__eleitores.append(eleitor)

        for candidato in self.__candidatos:
            self.__votos[candidato.get_numero()] = 0
        self.__votos['BRANCO'] = 0
        self.__votos['NULO'] = 0

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def get_eleitor(self, titulo: int):
        for eleitor in self.__eleitores:
            if eleitor.get_titulo() == titulo:
                return eleitor
        return False

    def registrar_voto(self, eleitor: Eleitor, n_cand: int):
        self.__eleitores_presentes.append(eleitor)
        if n_cand in self.__votos:
            self.__votos[n_cand] += 1
        elif n_cand == 0:
            self.__votos['BRANCO'] += 1
        else:
            self.__votos['NULO'] += 1

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    # Método para exportar para CSV
    def to_csv(self, file_name='urna.csv'):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Seção', 'Zona', 'Título dos Eleitores Presentes'])
            for eleitor in self.__eleitores_presentes:
                writer.writerow([self.__secao, self.__zona, eleitor.get_titulo()])


    # Método para exportar para TXT
    def to_txt(self, file_name='urna.txt'):
        with open(file_name, mode='w') as file:
            file.write(f'Seção: {self.__secao}\n')
            file.write(f'Zona: {self.__zona}\n')
            file.write('Título dos Eleitores Presentes:\n')
            for eleitor in self.__eleitores_presentes:
                file.write(f'- {eleitor.get_titulo()}\n')


    def __str__(self):
        data_atual = date.today()
        info = (f'Urna da seção {self.__secao}, zona {self.__zona}\n'
                f'Mesario {self.mesario}\n'
                f'{data_atual.ctime()}\n')

        for k, v in self.__votos.items():
            info += f'{k} = {v} votos\n'

        return info

    def zeresima(self):
        with open(f'{self.__nome_arquivo}_zer.pkl', 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def encerrar(sel):
        with open(f'{self.__nome_arquivo}_final.pkl', 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

if __name__ == "__main__":
    c1 = Candidato("lula","1234-2","123557-9", 13)
    c2 = Candidato("bolsonaro","56234-6","0967-5",22)

    e1= Eleitor("gabriel", "123-3","124678-5",1, 54,272)
    e2 = Eleitor("Breno", "27835-7", "40956-3",2,54,272)

    urna= Urna(e1, 54, 272,[c1,c2],[e1,e2])
    urna.registrar_voto(e2,13)
    urna.to_csv()
    urna.to_txt()