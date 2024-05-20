import csv
import os
from datetime import datetime, timedelta


def tabela(matriz_inicial):
    from tabulate import tabulate
    tabela = tabulate(matriz_inicial, headers="firstrow", tablefmt="grid")
    return tabela
    
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
    
def busca_data(matriz):
    data=input("Digite a data que deseja verificar")
    for linha in matriz:
        if linha[0] == data:
                print("bairro:",linha[1],"habitantes:",linha[2],"suspeitos:",linha[3],"negados:",linha[4],"confirmados:",linha[5])

def busca_bairro(matriz):
    bairro=input("Digite o bairro que deseja verificar")
    for linha in matriz:
        if linha[1] == bairro:
            print("data:",linha[0],"habitantes:",linha[2],"suspeitos:",linha[3],"negados:",linha[4],"confirmados:",linha[5])

def busca_intervalo(matriz):
    data1=input("Digite a primeira data")
    data2=input("Digite a segunda data")
    for linha in matriz:
        if data1==linha:
            print(linha)

def acrescentar_data(matriz):
    data=input("digite a data a acrescentar")
    matriz[].append(data)

#Menu Principal
Menu_principal=0
while Menu_principal!=3:
    print(os.getcwd()) 
    Menu_principal=int(input("[1]Informações sobre a dengue\n[2]Cadastro\n[3]Sair\nOpção:"))
    if Menu_principal==1:
        Menu_secundário=int(input("[1]Informações por data específica\n[2]Informações por bairro\n[3]Informações por intervalo de data\nOpção:"))
        if Menu_secundário==1:
            busca_data(matriz_inicial())   
        elif Menu_secundário==2:
            busca_bairro(matriz_inicial())
        elif Menu_secundário==3:
            busca_intervalo(matriz_inicial())
    elif Menu_principal==2:

print('Fechando programa')
