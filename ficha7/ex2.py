import os
def lerFicheiro():
    """
    ler ficheiro de temperaturas e devolve uma lista com o conteudo 
    """
    filetemp = open(ficheiro, 'r')
    listatemp = filetemp.readlines()
    filetemp.close()
    return listatemp

def guardarFicheiro(data, hora, temp):
    filetemp = open (ficheiro, "a", encoding = "utf-8")
    linha = data + ";" + hora + ";" + temp + "\n"
    filetemp.write(linha)
    filetemp.close()

#-----------------------------------#
def consulta_data():
    os.system("cls")
    data = input("Introduza uma data(ano-mes-dia): ")
    
    listatemp = lerFicheiro()
    for linha in listatemp:
        campos = linha.split(";")
        if data == campos[0].strip("\n"):
            print(campos[0],campos[1],campos[2])
    input()

#-----------------------------------#
def consulta_est():
    lTemps= []  # Lista vai conter APENAS com temperaturas do ficheiro
    listaTemp = lerFicheiro()       # ler fx. temperatura-txt
    for linha in listaTemp:         ## ler lista com dados do fx
        campos = linha.split(";")
        lTemps.append(int(campos[2].strip('\n')))
    
    print("\n\n\n\t\tO Maior valor de temperatura registada foi de:" , max(lTemps))
    print("\n\n\n\t\tO Menor valor de temperatura registada foi de:" , min(lTemps))
    print("\n\n\n\t\tO valor médio de temperatura registada foi de:" , sum(lTemps)/ len(lTemps))
    input()
    
    


ficheiro = ".\\files\\temperatura.txt"
def menu():
    while True:
        os.system("cls")
        print("\nMENU")
        print("1 - Consulta por data")
        print("2 - Consulta Estatisticas")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            consulta_data()
        elif opcao == '2':
            consulta_est()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Chama o menu
menu()
