# Inicializa o parque com 3 filas e 5 lugares cada, todos livres (0 = livre, 1 = ocupado)
parque = [[0] * 5 for _ in range(3)]

while True:
    # Exibe o menu
    print("\nMENU")
    print("1 - Entrada de veículo")
    print("2 - Saída de carro")
    print("3 - Estado do Parque")
    print("0 - Sair")
    opcao = input("Escolha uma das opções: ")

    if opcao == "1":
        # Entrada de veículo
        ocupado = False
        for i in range(3):        # Percorre as filas
            for j in range(5):    # Percorre os lugares em cada fila
                if parque[i][j] == 0:  # Verifica se o lugar está livre
                    parque[i][j] = 1   # Ocupa o lugar
                    print(f"Veículo estacionado na posição: Fila {i+1}, Lugar {j+1}")
                    ocupado = True
                    break  # Sai do loop ao encontrar o primeiro lugar livre
            if ocupado:
                break
        if not ocupado:
            print("Parque completo")

    elif opcao == "2":
        # Saída de veículo
        fila = int(input("Digite a fila do veículo (1-3): ")) - 1
        lugar = int(input("Digite o lugar do veículo (1-5): ")) - 1
        if 0 <= fila < 3 and 0 <= lugar < 5:
            if parque[fila][lugar] == 1:
                parque[fila][lugar] = 0  # Libera o lugar
                print(f"Veículo removido da posição: Fila {fila+1}, Lugar {lugar+1}")
            else:
                print("O lugar já está vazio.")
        else:
            print("Posição inválida.")

    elif opcao == "3":
        # Estado do Parque
        ocupados = sum(sum(fila) for fila in parque)  # Conta o total de lugares ocupados
        livres = 15 - ocupados  # Calcula os lugares livres
        print(f"Lugares ocupados: {ocupados}")
        print(f"Lugares livres: {livres}")

    elif opcao == "0":
        # Sair do programa
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
