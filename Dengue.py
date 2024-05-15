import csv
import os

linha=0


def ler():
    arquivo_csv=("DadosDengue.csv")
    with open("DadosDengue.csv","r",) as arquivo_csv:
        leitor_csv=csv.reader(arquivo_csv,delimiter=",")
        for linha in leitor_csv:
            print(linha)
            

def alterar():
    arquivo_csv=("DadosDengue.csv")
    dados=[arquivo_csv]
        # with open("DadosDengue.csv","w") as arquivo_csv:
        #     editor_csv=csv.writer(arquivo_csv,delimiter="")


def adicionar():
    arquivo_csv=("DadosDengue.csv")
    with open("DadosDengue.csv","r",) as arquivo_csv:
        leitor_csv=csv.reader(arquivo_csv,delimiter=",")
        for linha in leitor_csv:
            lista_csv.append(linha)
            

def ler_por_data():
    data=int(input("Digite a data que deseja verificar"))
    if linha[0] == data:
        print(linha)



Menu_principal=0
while Menu_principal!=3:
    print(os.getcwd()) 
    Menu_principal=int(input("[1]Informações sobre a dengue\n[2]Cadastro\n[3]Sair\nOpção:"))
    if Menu_principal==1:
        ler()    
    elif Menu_principal==2:
        alterar()
print('Fechando programa')
