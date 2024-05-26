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
from tkinter import filedialog
from datetime import datetime, timedelta

#limpa terminal
#print(chr(27)+ "[2j")
#filedialog.askopenfilename (title = “Dados_Dengue.csv”, filetypes = ((“file_type”, ”*.csv”), (“all files”, ”*. *”)))

#lê o arquivo csv e transforma em lista
def matriz_inicial():
    with open("DadosDengue.csv","r",) as arquivo_csv:
        leitor_csv=csv.reader(arquivo_csv,delimiter=",")
        lista_csv=[]
        for item in leitor_csv:
            lista_csv.append(item)
        lista_csv.pop(0) # Remove cabeçalho
        return lista_csv
    
def matriz_colunas():
    with open("DadosDengue.csv","r",) as arquivo_csv:
        leitor_csv=csv.reader(arquivo_csv,delimiter=",")
        coluna=[]
        for item in leitor_csv:
           coluna.append(item)
        coluna.pop(0) 
        return coluna
    

#Formata e imprime a matriz
def adicionar(matriz):
    for linha in matriz:
        print('{:>10}{:>15}|{:>10}{:>15}|{:>10}{:>15}|{:>10}{:>15}|{:>10} {:>15}'.format(
    "DATA:",linha[0],
    "BAIRRO:", linha[1], 
    "SUSPEITOS:", linha[3], 
    "NEGADOS:", linha[4], 
    "CONFIRMADOS:", linha[5]))

#converte elementos de lista referentes aos casos em inteiros
def converter(matriz):
    casos_sus = [int(linha[3]) for linha in matriz]
    casos_neg = [int(linha[4]) for linha in matriz]
    casos_pos = [int(linha[5]) for linha in matriz]
    return casos_pos,casos_neg,casos_sus

#===============================================SEÇÃO DE PESQUISA=============================================================

#percorre a matriz e seleciona a linha onde a entrada corresponde com o índice 0 da lista (datas)     
def busca_data(matriz):
    data=input("Por favor,informe a data deseja verificar:\n")
    for linha in matriz:
        if linha[0] == data:
            print('{:>10}{:>15}|{:>10}{:>15}|{:>10}{:>15}|{:>10}{:>15}|{:>10} {:>15}'.format(
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
            print('{:>10}{:>15}|{:>10}{:>15}|{:>10}{:>15}|{:>10}{:>15}|{:>10} {:>15}'.format(
    "DATA:", linha[0], 
    "HABITANTES:", linha[2], 
    "SUSPEITOS:", linha[3], 
    "NEGADOS:", linha[4], 
    "CONFIRMADOS:", linha[5]
))

#Exibe dados referentes ao intervalo de datas informado pelo usuário
def busca_intervalo(matriz):
    coluna=matriz_colunas()
    data1=input("Digite a primeira data:")
    data2=input("Digite a segunda data:")
    for linha in matriz:
        if coluna[0]==data1 and coluna[26]:
            print('{:>10}{:>15}|{:>10}{:>15}|{:>10}{:>15}|{:>10}{:>15}|{:>10} {:>15}'.format(
        "HABITANTES:", linha[2], 
        "SUSPEITOS:", linha[3], 
        "NEGADOS:", linha[4], 
        "CONFIRMADOS:", linha[5]))

# Exibe porcentagem de casos positivos e negativos em relação ao total
def porcentagem_geral(matriz):
    casos_pos, casos_neg, casos_sus = converter(matriz)
    soma_cs=sum(casos_sus) 
    soma_cn=sum(casos_neg)
    soma_cp=sum(casos_pos)
    total=soma_cp+soma_cn+soma_cs
    porcentagem_positivos=soma_cp*(100/total)
    porcentagem_negativos=soma_cn*(100/total)
    print('|------INDICADORES DE PREVALÊNCIA------|')
    print(f'Positivos:',"%.1f" %porcentagem_positivos,'% ''Negativos:', "%.1f" %porcentagem_negativos,'%') 

#===============================================SEÇÃO DE EDIÇÃO=============================================================

#solicita novos casos suspeitos e substitui no índice 3 da matriz,referente aos suspeito
def alterar_suspeitos(matriz):
    casos_sus = converter(matriz)
    bairro=input("Esses dados são referentes a qual localidade? \n(OBS:Informar com base no endereço)")
    suspeitos_soma=int(input("Informe a quantidade de suspeitos que foram positivados: "))
    for linha in matriz:
        return linha
    if linha[1] == bairro :
        linha[3] = str(int(linha[3]) + suspeitos_soma)
    print(f"No bairro {bairro},houve um acréscimo de {suspeitos_soma} casos positivos totalizando {linha[3]}")

#solicita novos casos positivos e substitui no índice 5 da matriz,referente aos positivos
def alterar_positivados(matriz):
    casos_pos,casos_sus = converter(matriz)
    positivos_soma=int(input("Informe a quantidade de suspeitos que foram positivados: "))
    bairro=input("Esses dados são referentes a qual localidade? \n(OBS:Informar com base no endereço)")
    for linha in matriz:
        if linha[1] == bairro :
            casos_pos+= positivos_soma
            casos_sus-=casos_pos
        # print(f"No bairro {bairro},houve um acréscimo de {positivos_soma} casos positivos totalizando {casos_pos}")

#solicita novos casos negativos,por dia e data e substitui no índice 4 da matriz,referente aos negativos
def alterar_negativados(matriz):
    casos_neg, casos_sus = converter(matriz)
    negativos_soma=int(input("Informe a quantidade de suspeitos que foram positivados: "))
    bairro=input("Esses dados são referentes a qual localidade? \n(OBS:Informar com base no endereço)")
    for linha in matriz:
        if linha[1] == bairro :
            casos_neg+= negativos_soma
            casos_sus-=casos_neg
        # print(f"No bairro {bairro},houve um acréscimo de {negativos_soma} casos positivos totalizando {casos_neg}")

#===============================================SEÇÃO PRINCIPAL=============================================================

#função principal:Menus
def main():
    #Menu Principal
    Menu_principal=0
    while Menu_principal!=3:
        print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
        Menu_principal=int(input("[1]Informações sobre a dengue\n[2]Cadastro\n[3]Sair\nOpção:"))
        if Menu_principal==1:
            print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
            Menu_Secundário_busca=int(input("[1]Informações por data específica\n\n[2]Informações por bairro\n\n[3]Informações por intervalo de data\n\n[4]Indicadores de prevalência\n\n[5]Boletim completo\n\nOpção:"))
            if Menu_Secundário_busca==1:
                print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
                busca_data(matriz_inicial())   
            elif Menu_Secundário_busca==2:
                print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
                busca_bairro(matriz_inicial())
            elif Menu_Secundário_busca==3:
                print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
                busca_intervalo(matriz_inicial())
            elif Menu_Secundário_busca==4:
                porcentagem_geral(matriz_inicial())
            elif Menu_Secundário_busca==5:
                adicionar(matriz_inicial())
        elif Menu_principal==2:
            print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
            Menu_secundário_edição=int(input("Alterar número de:\n[1]Suspeitos de dengue \n\n[2]Casos positivos\n\n[3]Casos negativos\n"))
            if Menu_secundário_edição==1:
                alterar_suspeitos(matriz_inicial())
            if Menu_secundário_edição==2:
                alterar_positivados(matriz_inicial())
            if Menu_secundário_edição==3:
                alterar_negativados(matriz_inicial())
                
    print('Fechando programa')

#Retorna a função principal sempre que sua execução chega ao fim
if __name__ == "__main__":
    main()
