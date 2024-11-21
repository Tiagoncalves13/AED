# Caminho fixo para o ficheiro paises.txt
FILE_PATH = "files/paises.txt"

# Função para garantir que o ficheiro e a pasta existem
def garantir_ficheiro_existe():
    try:
        with open(FILE_PATH, "r") as f:
            pass
    except FileNotFoundError:
        # Cria o ficheiro e pasta se não existirem
        try:
            os.mkdir("files")
        except FileExistsError:
            pass
        with open(FILE_PATH, "w") as f:
            pass

# Função para inserir um novo país
def inserir_pais():
    garantir_ficheiro_existe()
    pais = input("Insira o nome do país: ").strip()
    continente = input("Insira o continente: ").strip()
    
    with open(FILE_PATH, "r") as f:
        linhas = f.readlines()
    
    # Verifica se o país já existe
    for linha in linhas:
        if linha.startswith(pais + ";"):
            print("Este país já existe no ficheiro.")
            return
    
    # Adiciona o país ao ficheiro
    with open(FILE_PATH, "a") as f:
        f.write(f"{pais};{continente}\n")
    print("País adicionado com sucesso.")

# Função para listar todos os países
def consultar_paises():
    garantir_ficheiro_existe()
    with open(FILE_PATH, "r") as f:
        linhas = f.readlines()
    
    if not linhas:
        print("O ficheiro está vazio.")
    else:
        print("Países no ficheiro:")
        for linha in linhas:
            pais, continente = linha.strip().split(";")
            print(f"País: {pais}, Continente: {continente}")

# Função para consultar países por continente
def consultar_por_continente():
    continente_procurado = input("Insira o continente: ").strip()
    garantir_ficheiro_existe()
    
    with open(FILE_PATH, "r") as f:
        linhas = f.readlines()
    
    encontrados = [linha.split(";")[0] for linha in linhas if linha.strip().endswith(continente_procurado)]
    
    if encontrados:
        print(f"Países no continente {continente_procurado}:")
        for pais in encontrados:
            print(pais)
    else:
        print(f"Nenhum país encontrado no continente {continente_procurado}.")

# Função para contar o número de países por continente
def consultar_num_paises_por_continente():
    garantir_ficheiro_existe()
    continentes = {}
    
    with open(FILE_PATH, "r") as f:
        linhas = f.readlines()
    
    for linha in linhas:
        pais, continente = linha.strip().split(";")
        if continente not in continentes:
            continentes[continente] = 0
        continentes[continente] += 1
    
    if not continentes:
        print("O ficheiro está vazio.")
    else:
        print("Número de países por continente:")
        for continente, count in continentes.items():
            print(f"{continente}: {count} países")

# Função principal com o menu
def menu():
    while True:
        print("\nMENU")
        print("1 - Inserir Países")
        print("2 - Consultar Países")
        print("3 - Consultar por Continente")
        print("4 - Consultar nº de Países por Continente")
        print("0 - Sair")
        
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == "1":
            inserir_pais()
        elif escolha == "2":
            consultar_paises()
        elif escolha == "3":
            consultar_por_continente()
        elif escolha == "4":
            consultar_num_paises_por_continente()
        elif escolha == "0":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu principal
menu()
