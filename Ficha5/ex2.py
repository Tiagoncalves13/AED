import random  # Importa a biblioteca para gerar números aleatórios

# Função para inicializar a matriz com valores aleatórios
def inicializar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = [random.randint(10, 100) for _ in range(colunas)]  # Gera uma linha com valores aleatórios
        matriz.append(linha)
    print("\nMatriz Gerada:")
    for linha in matriz:
        print(linha)
    return matriz

# Função para calcular a matriz transposta
def matriz_transposta(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0]) if linhas > 0 else 0
    transposta = []
    for i in range(colunas):
        linha_transposta = [matriz[j][i] for j in range(linhas)]
        transposta.append(linha_transposta)
    print("\nMatriz Transposta:")
    for linha in transposta:
        print(linha)

# Função para encontrar o maior valor da matriz
def maior_valor(matriz):
    maior = max(max(linha) for linha in matriz)  # Encontra o maior valor em todas as linhas
    print(f"\nMaior valor da matriz: {maior}")

# Programa principal
matriz = None

while True:
    # Exibe o menu
    print("\nMENU")
    print("1 - Inicializar matriz")
    print("2 - Matriz Transposta")
    print("3 - Maior valor")
    print("Ø - Sair")
    opcao = input("Escolha uma das opções: ")

    if opcao == "1":
        # Inicializar a matriz com dimensões definidas pelo usuário
        linhas = int(input("Digite o número de linhas da matriz: "))
        colunas = int(input("Digite o número de colunas da matriz: "))
        matriz = inicializar_matriz(linhas, colunas)

    elif opcao == "2":
        # Verificar se a matriz foi inicializada antes de calcular a transposta
        if matriz is not None:
            matriz_transposta(matriz)
        else:
            print("A matriz ainda não foi inicializada. Por favor, inicialize a matriz primeiro.")

    elif opcao == "3":
        # Verificar se a matriz foi inicializada antes de encontrar o maior valor
        if matriz is not None:
            maior_valor(matriz)
        else:
            print("A matriz ainda não foi inicializada. Por favor, inicialize a matriz primeiro.")

    elif opcao == "Ø" or opcao.lower() == "0":
        # Sair do programa
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
