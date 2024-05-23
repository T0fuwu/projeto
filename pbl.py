#Autor: Maria Clara Nunes Ramos
#Componente Curricular: Algoritmos I
#Concluido em:/0/2024
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

import csv
import os
#from datetime import datetime, timedelta



#limpa o terminal
def limpar_terminal():
    if os.system == 'Windows':
        os.system('cls')

#lê o arquivo csv e transforma em lista
def matriz_inicial():
    with open("DadosDengue.csv","r",) as arquivo_csv:
        leitor_csv=csv.reader(arquivo_csv,delimiter=",")
        lista_csv=[]
        for i, item in enumerate(leitor_csv):
            if i != 0:
                lista_csv.append(item)
        return lista_csv

#transforma o arquivo csv em matriz
def adicionar(matriz):
    for item in matriz:
        print(item)

#percorre a matriz e seleciona a linha onde a entrada corresponde com o índice 0 da lista (datas)     
def busca_data(matriz):
    data=input("Por favor,informe a data deseja verificar:\n")
    for linha in matriz:
        if linha[0] == data:
            print('{:>20}  {:>20} | {:>20}  {:>20} | {:>20}  {:>20}'.format(
    "BAIRRO:", linha[1], 
    "HABITANTES:", linha[2], 
    "SUSPEITOS:", linha[3], 
    "NEGADOS:", linha[4], 
    "CONFIRMADOS:", linha[5]
))

#percorre a matriz e seleciona a linha onde a entrada corresponde com o índice 1 da lista (bairros)
def busca_bairro(matriz):
    bairro=input("Por favor,informe o bairro que deseja verificar:\n")
    for linha in matriz:
        if linha[1] == bairro:
            print('{:>20}  {:>20} | {:>20}  {:>20} | {:>20}  {:>20}'.format(
    "DATA:", linha[0], 
    "HABITANTES:", linha[2], 
    "SUSPEITOS:", linha[3], 
    "NEGADOS:", linha[4], 
    "CONFIRMADOS:", linha[5]
))

def busca_intervalo(matriz):
    data1=input("Digite a primeira data")
    data2=input("Digite a segunda data")

def porcentagem(matriz):
    cs = [int(linha[3]) for linha in matriz]
    cn = [int(linha[3]) for linha in matriz]
    cp = [int(linha[3]) for linha in matriz]
    soma_cs=sum(cs) 
    soma_cn=sum(cn)
    soma_cp=sum(cp)
    total=soma_cp+soma_cn+soma_cs
    porcentagem_positivos=soma_cp*(100/total)
    porcentagem_negativos=soma_cn*(100/total)
    print('|------INDICADORES DE PREVALÊNCIA------|')
    print(f'Positivos:',"%.1f" %porcentagem_positivos,'%''Negativos:', "%.1f" %porcentagem_negativos,'%') 
     
#acrescenta uma entrada no índice 0 da matriz,referente a data
def acrescentar_data(matriz):
    data=input("digite a data a acrescentar")
    for linha in matriz:
        linha[0].append(data)
    
#solicita novos casos positivos e substitui no índice 5 da matriz,referente aos positivos
def alterar_positivados(matriz):
    positivos_soma= input("Informe a quantidade de suspeitos que foram positivados: ")
    suspeitos-=positivos_soma

def alterar_suspeitos(matriz):
    suspeitos_novos= input("Informe a quantidade de suspeitos novos: ")

def alterar_negativados(matriz):
    negativos_soma= input("Informe a quantidade de suspeitos que foram negativados: ")
    suspeitos-=negativos_soma

def alterar_positivos(matriz):
    positivos_soma= input("Informe a quantidade de suspeitos que foram negativados: ")
    
def main():
    #Menu Principal
    Menu_principal=0
    while Menu_principal!=3:
        #print(os.getcwd()) 
        print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
        Menu_principal=int(input("[1]Informações sobre a dengue\n[2]Cadastro\n[3]Sair\nOpção:"))
        if Menu_principal==1:
            print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
            Menu_secundário=int(input("[1]Informações por data específica\n\n[2]Informações por bairro\n\n[3]Informações por intervalo de data\n\n[4]Indicares de prevalência\n\n[5]Boletim completo\n\nOpção:"))
            if Menu_secundário==1:
                print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
                busca_data(matriz_inicial())   
                limpar_terminal()
            elif Menu_secundário==2:
                print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
                busca_bairro(matriz_inicial())
                limpar_terminal()
            elif Menu_secundário==3:
                print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
                busca_intervalo(matriz_inicial())
                limpar_terminal()
            elif Menu_secundário==4:
                porcentagem(matriz_inicial())
            elif Menu_secundário==5:
                adicionar(matriz_inicial())
                limpar_terminal()
        elif Menu_principal==2:
            print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
    print('Fechando programa')

if __name__ == "__main__":
    main()
