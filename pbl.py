#Autor: Maria Clara Nunes Ramos
#Componente Curricular: Algoritmos I
#Concluido em:/05/2024
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

import csv
import os
from datetime import datetime, timedelta
from tkinter import filedialog as fd


                      
#filedialog.askopenfilename (title = “Dados_Dengue.csv”, filetypes = ((“file_type”, ”*.csv”), (“all files”, ”*. *”)))
# filename=input('Nome do arquivo')    
# filename = fd.askopenfilename()

#================================================SEÇÃO DE FORMATAÇÃO==========================================================

#lê o arquivo csv e transforma em lista
def matriz_inicial():
    with open("DadosDengue.csv","r",) as arquivo_csv:
        leitor_csv=csv.reader(arquivo_csv,delimiter=",")
        lista_csv=[]
        for linha in leitor_csv:
            lista_csv.append(linha)
        lista_csv.pop(0) # Remove cabeçalho
        return lista_csv
    
    
#Imprime a matriz
def adicionar(matriz):
    for linha in matriz:
        print('{:>10}{:>15}|{:>10}{:>15}|{:>10}{:>15}|{:>10}{:>15}|{:>10} {:>15}|{:>10} {:>15}'.format(
    "DATA:",linha[0],
    "BAIRRO:", linha[1], 
    "HABITANTES",linha[2],
    "SUSPEITOS:", linha[3], 
    "NEGADOS:", linha[4], 
    "CONFIRMADOS:", linha[5]))

#Cria um arquivo csv
def escrever_csv():
    molde_arquivo = ['Data', 'Bairros', 'Habitantes', 'Casos Suspeitos', 'Casos Negativos', 'Casos Confirmados']
    with open('DadosDengue', 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(molde_arquivo)

#Limpa o terminal 
def limpa_terminal():
    os.system('cls') or None

# Retrna a última data 
def última_data(matriz):
    dados=[]
    última_data = matriz[-1][0]
    for linha in matriz:
        if linha[0]==última_data:
            dados.append(linha)
    return linha

# Converte tipo dos elementos da matriz do csv em para inteiro
def converter(matriz):
    casos_sus = [int(linha[3]) for linha in matriz]
    casos_neg = [int(linha[4]) for linha in matriz]
    casos_pos = [int(linha[5]) for linha in matriz]
    return casos_sus,casos_neg,casos_sus


def porcentagem_geral(matriz):
            casos_pos, casos_neg, casos_sus = converter(matriz)
            soma_cs=sum(casos_sus) 
            soma_cn=sum(casos_neg)
            soma_cp=sum(casos_pos)
            total=soma_cp+soma_cn+soma_cs
            porcentagem_positivos=soma_cp*(100/total)
            porcentagem_negativos=soma_cn*(100/total)
            for linha in matriz:
                if linha[0] == matriz[-1][0]:
                    print('|------INDICADORES DE PREVALÊNCIA------|')
                    print(f'Positivos: {"%.1f" % porcentagem_positivos}%, Negativos: {"%.1f" % porcentagem_negativos}%')
                    return linha 


# Exibe porcentagem de casos positivos e negativos em relação ao total de habiitantes por bairro
def porcentagem_bairro(matriz):
    bairro = input("Por favor, informe o bairro que deseja verificar:\n")
    linha=matriz_inicial()
    casos_neg,casos_pos,casos_sus = converter(matriz)
    hab=([int(linha(2))]for linha in matriz if linha[linha[1]]==bairro)
    porcentagem_positivos=casos_pos*(100/hab)
    porcentagem_negativos=casos_neg*(100/hab)
    print('|------INDICADORES DE PREVALÊNCIA------|')
    print(f'Positivos: {"%.1f" % porcentagem_positivos}%, Negativos: {"%.1f" % porcentagem_negativos}%')

            
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

# Exibe dados referentes ao intervalo de datas informado pelo usuário
def busca_intervalo(matriz):
    data1_str = input("Digite a primeira data (formato DD/MM/AAAA):\n")
    data2_str = input("Digite a segunda data (formato DD/MM/AAAA):\n")
    data1 = datetime.strptime(data1_str, "%d/%m/%Y")
    data2 = datetime.strptime(data2_str, "%d/%m/%Y")
    print("\nLinhas dentro do intervalo de datas:\n")
    for linha in matriz:
        data_atual = datetime.strptime(linha[0], "%d/%m/%Y")
        if data1 <= data_atual <= data2:
            print('{:>10}{:>15}|{:>10}{:>15}|{:>10}{:>15}|{:>10}{:>15}|{:>10} {:>15}'.format(
                "DATA:", linha[0],
                "BAIRRO:", linha[1], 
                "HABITANTES:", linha[2], 
                "SUSPEITOS:", linha[3], 
                "NEGADOS:", linha[4], 
                "CONFIRMADOS:", linha[5]))

#===============================================SEÇÃO DE EDIÇÃO=============================================================
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

#solicita novos casos negativos,por dia e data e substitui no índice 3 da matriz,referente aos negativos
def alterar_suspeitos(matriz):
    casos_sus = converter(matriz)
    suspeitos=int(input("Informe a quantidade de suspeitos que foram positivados: "))
    bairro=input("Esses dados são referentes a qual localidade? \n(OBS:Informar com base no endereço)")
    for linha in matriz:
        if linha[1] == bairro :
            casos_sus+= suspeitos
            
# Adicionar novas datas à matriz
def adicionar_datas(matriz):
    data = matriz[-1][0]  
    ultima_data = datetime.strptime(data, "%d/%m/%Y")
    proxima_data = ultima_data + timedelta(days=1)
    nova_linha = [proxima_data.strftime("%d/%m/%Y"), '', '', 0, 0, 0]
    matriz.append(nova_linha)
    print("Nova data adicionada:", proxima_data.strftime("%d/%m/%Y"))

#===============================================SEÇÃO PRINCIPAL=============================================================

#função principal:Menus
def main():
    #Menu Principal
    Menu_principal=0
    while Menu_principal!=3:
        print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
        Menu_principal=int(input("[1]Informações sobre a dengue\n[2]Cadastro\n[3]Sair\nOpção:"))
        limpa_terminal()
        if Menu_principal==1:
            print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
            Menu_Secundário_busca=int(input("[1]Informações por data específica\n\n[2]Informações por bairro\n\n[3]Informações por intervalo de data\n\n[4]Indicadores de prevalência\n\n[5]Boletim completo\n\nOpção:"))
            limpa_terminal()
            
            if Menu_Secundário_busca==1:
                print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
                busca_data(matriz_inicial())
                adicionar_datas(matriz_inicial()) 
           
            elif Menu_Secundário_busca==2:
                print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
                busca_bairro(matriz_inicial())
            
            elif Menu_Secundário_busca==3:
                print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
                busca_intervalo(matriz_inicial())
            
            elif Menu_Secundário_busca==4:
                Menu_terciário=int(input("[1]Informação geral\n\n[2]Informação por bairro\n"))
                limpa_terminal()
                if Menu_terciário==1:
                    porcentagem_geral(matriz_inicial())
                elif Menu_terciário==2:
                    porcentagem_bairro(matriz_inicial())
            
            elif Menu_Secundário_busca==5:
                adicionar(matriz_inicial())
    
        
        
        elif Menu_principal==2:
            print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
            Menu_secundário_edição=int(input("Alterar número de:\n[1]Suspeitos de dengue \n\n[2]Casos positivos\n\n[3]Casos negativos\n"))
            limpa_terminal()
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
