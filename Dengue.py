import csv
import os
Menu_principal=0
while Menu_principal!=3:
    print(os.getcwd())
    Menu_principal=int(input("[1]Informações sobre a dengue\n[2]Cadastro\n[3]Sair\nOpção:"))
    if Menu_principal==1:
        arquivo_csv=("DadosDengue.csv")
        with open("DadosDengue.csv","r",) as arquivo_csv:
            leitor_csv=csv.reader(arquivo_csv,delimiter=",")
            for linha in leitor_csv:
                print(linha)
    elif Menu_principal==2:
        arquivo_csv=("DadosDengue.csv")
        dados=[arquivo_csv]
        # with open("DadosDengue.csv","w") as arquivo_csv:
        #     editor_csv=csv.writer(arquivo_csv,delimiter=",")
        print("alteração")
print('Fechando programa')
