import csv
import os
from datetime import datetime, timedelta

def tabela(matriz_inicial):
    from tabulate import tabulate
    tabela = tabulate(matriz_inicial, headers="firstrow", tablefmt="grid")
    return tabela



#def ler():
#    arquivo_csv=("DadosDengue.csv")
#    with open("DadosDengue.csv","r",) as arquivo_csv:
#        leitor_csv=csv.reader(arquivo_csv,delimiter=",")
#        for linha in leitor_csv:
#            print(linha)
            

#def alterar(matriz):
    
def matriz_inicial():
    with open("DadosDengue.csv","r",) as arquivo_csv:
        leitor_csv=csv.reader(arquivo_csv,delimiter=",")
        lista_csv=[]
        for item in leitor_csv:
            lista_csv.append(item)
        return lista_csv


def adicionar(matriz):
    for item in matriz:
        print(item)
    
            

def ler_por_data(matriz):
    data=int(input("Digite a data que deseja verificar"))
    if linha[0] == data:
        print(linha)



Menu_principal=0
while Menu_principal!=3:
    print(os.getcwd()) 
    Menu_principal=int(input("[1]Informações sobre a dengue\n[2]Cadastro\n[3]Sair\nOpção:"))
    if Menu_principal==1:
        adicionar(matriz_inicial())
    elif Menu_principal==2:
        adicionar()
print('Fechando programa')
