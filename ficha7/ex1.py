# Função para garantir que o ficheiro de países existe
def garantir_ficheiro():
    try:
        open('files/paises.txt', 'r').close()  # Tenta abrir para leitura
    except FileNotFoundError:
        with open('files/paises.txt', 'w', encoding='utf-8') as f:
            pass  # Cria o ficheiro vazio se não existir

# Função para inserir um novo país no ficheiro
def inserir_pais():
    pais = input("Introduza o nome do país: ").strip()
    continente = input("Introduza o continente do país: ").strip()

    # Verifica se o país já existe no ficheiro
    with open('files/paises.txt', 'r', encoding='utf-8') as file:
        paises_existentes = file.readlines()

    # Verifica se o país já está no ficheiro
    for linha in paises_existentes:
        if pais in linha.split(';')[0]:
            print(f"O país {pais} já existe no ficheiro.")
            return

    # Se o país não existir, adiciona ao ficheiro
    with open('files/paises.txt', 'a', encoding='utf-8') as file:
        file.write(f"{pais};{continente}\n")
    print(f"País {pais} adicionado com sucesso!")

# Função para listar todos os países
def consultar_paises():
    with open('files/paises.txt', 'r', encoding='utf-8') as file:
        paises = file.readlines()

    if not paises:
        print("Não há países registrados.")
    else:
        for linha in paises:
            print(linha.strip())

# Função para consultar países por continente
def consultar_por_continente():
    continente = input("Introduza o nome do continente: ").strip()
    with open('files/paises.txt', 'r', encoding='utf-8') as file:
        paises = file.readlines()

    encontrados = [linha.strip() for linha in paises if continente in linha.split(';')[1]]
    
    if not encontrados:
        print(f"Não há países registrados no continente {continente}.")
    else:
        for pais in encontrados:
            print(pais)

# Função para contar o número de países por continente
def contar_paises_por_continente():
    with open('files/paises.txt', 'r', encoding='utf-8') as file:
        paises = file.readlines()

    continentes = {}
    for linha in paises:
        continente = linha.strip().split(';')[1]
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    for continente, count in continentes.items():
        print(f"Continente {continente}: {count} países")

# Função para exibir o menu
def menu():
    while True:
        print("\nMENU")
        print("1 - Inserir Países")
        print("2 - Consulta Países")
        print("3 - Consulta por Continente")
        print("4 - Consultar nº de países por continente")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            garantir_ficheiro()
            inserir_pais()
        elif opcao == '2':
            consultar_paises()
        elif opcao == '3':
            consultar_por_continente()
        elif opcao == '4':
            contar_paises_por_continente()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Chama o menu
menu()
