def gerenciar_fila():
    fila = [0] * 20  # Fila com 20 lugares livres (0 significa livre)
    
    while True:
        print("\nMENU")
        print("1 - Tirar Ticket")
        print("2 - Atendimento")
        print("3 - Estado da fila de espera")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':  # Tirar Ticket
            try:
                posicao = fila.index(0)  # Encontra a primeira posição livre
                fila[posicao] = posicao + 1  # Preenche com o número do ticket
                print(f"Ticket tirado! Sua posição é: {fila[posicao]}")
            except ValueError:
                print("Fila completa!")  # Não há mais lugares livres
        
        elif opcao == '2':  # Atendimento
            if fila[0] == 0:
                print("Não há ninguém na fila para atender.")
            else:
                print(f"Atendendo ticket número: {fila[0]}")
                # Avança a fila
                fila = fila[1:] + [0]  # Remove o primeiro e adiciona 0 no final
        
        elif opcao == '3':  # Estado da fila de espera
            ocupados = sum(1 for lugar in fila if lugar != 0)
            livres = fila.count(0)
            print(f"Lugares ocupados: {ocupados}, Lugares livres: {livres}")
        
        elif opcao == '0':  # Sair
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Executa a função
gerenciar_fila()
