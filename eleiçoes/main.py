import pickle
import traceback

from pessoas import *

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS= 'candidatos.pkl'


def menu_candidato():
    print("1-Novo candidato")
    print("2-Atualizar candidato")
    print("3-Sair")
    op = int(input("Digite a opcao [1,2,3]? "))
    while op not in (1, 2, 3):
        op = int(input("Digite a opcao [1,2,3]? "))
    return op

def inserir_candidato(candidatos):
    numero = int(input("Digite o numero: "))

    if numero in candidatos:
        raise Exception("numero já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")

    candidato = Candidato(nome, RG, CPF, numero)
    candidatos[candidato.get_numero()] = candidato

    with open(FILE_CANDIDATOS, 'wb') as arquivo:
        pickle.dump(candidatos, arquivo)

    print('Candidato gravado com sucesso!')
    print(candidato)

def atualizar_candidato(candidatos):
    nome = int(input('Digite o nome do candidato: '))

    if nome in candidatos:
        candidato = candidatos[nome]
        print(candidato)
        numero = input("Digite o novo numero: ")

        eleitor.numero = numero

        with open(FILE_ELEITORES, 'wb') as arquivo:
            pickle.dump(candidatos, arquivo)

        print('Atualizado dado do candidato!')
        print(candidato)
    else:
        raise Exception('Nome inexistente')
def listar_candidatos(candidatos):
    for c in candidatos.values():
        print(c)
def menu_eleitor():
    print("1-Novo Eleitor")
    print("2-Atualizar Eleitor")
    print("3-Sair")
    op = int(input("Digite a opcao [1,2,3]? "))
    while op not in (1, 2, 3):
        op = int(input("Digite a opcao [1,2,3]? "))
    return op

def inserir_eleitor(eleitores):
    titulo = int(input("Digite o Títlulo: "))

    if titulo in eleitores:
        raise Exception("Titulo já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")
    secao = input("Digite a secao: ")
    zona = input("Digite a zona: ")

    eleitor = Eleitor(nome, RG, CPF, titulo, secao, zona)
    eleitores[eleitor.get_titulo()] = eleitor

    with open(FILE_ELEITORES, 'wb') as arquivo:
        pickle.dump(eleitores, arquivo)

    print('Eleitor gravado com sucesso!')
    print(eleitor)


def atualizar_eleitor(eleitores):
    titulo = int(input('Digite o titulo do eleitor: '))

    if titulo in eleitores:
        eleitor = eleitores[titulo]
        print(eleitor)
        secao = input("Digite a nova secao: ")
        zona = input("Digite a nova zona: ")
        eleitor.secao = secao
        eleitor.zona = zona

        with open(FILE_ELEITORES, 'wb') as arquivo:
            pickle.dump(eleitores, arquivo)

        print('Atualizados dados do eleitor!')
        print(eleitor)
    else:
        raise Exception('Titulo inexistente')

if __name__ == "__main__":
    candidatos = {}
    eleitores = {} #dicionário a chave será o titulo
    try:
        print("Carregando arquivos de dados ...")
        with open(FILE_ELEITORES, 'rb') as arquivo:
            eleitores = pickle.load(arquivo)
        with open(FILE_CANDIDATOS, 'rb') as arquivo:
            candidatos = pickle.load(arquivo)

    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado!")

    opcao = "1"
    while opcao in ("1","2","3"):
        try:
            op_user = "0"
            while op_user not in ("1","2"):
                op_user = input("1-gerenciar eleitor\n"+
                                "2-gerenciar candidato\n")
            if op_user == "1":
                opcao = menu_eleitor()
                if opcao ==1:
                    inserir_eleitor(eleitores)
                if opcao == 2:
                    atualizar_eleitor(eleitores)
                if opcao == 3:
                    print("saindo")
                    break
            else:
                opcao = menu_candidato()
                if opcao == 1:
                    inserir_candidato(candidatos)
                elif opcao == 2:
                    atualizar_candidato(candidatos)
                elif opcao == 3:
                    print("Saindo!")
                    break
        except Exception as e:
            traceback.print_exc()
            print(e)