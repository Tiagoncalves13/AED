def visitantes_exposicao():
    dias = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]
    visitantes = [int(input(f"Digite o número de visitantes em {dia}: ")) for dia in dias]

    # Ordena os visitantes em ordem decrescente
    visitantes_ordenados = sorted(visitantes, reverse=True)

    # Imprime a lista de visitantes
    print("\nNúmero de visitantes por dia (ordem decrescente):")
    for dia, num in zip(dias, visitantes_ordenados):
        print(f"{dia}: {num}")

    # Calcula a média
    media = sum(visitantes) / len(visitantes)
    print(f"\nNúmero médio de visitantes por dia: {media:.2f}")

    # Encontra o dia mais próximo da média
    dia_proximo = dias[visitantes.index(min(visitantes, key=lambda x: abs(x - media)))]
    print(f"O dia que mais se aproximou da média é: {dia_proximo}")

# Executa a função
visitantes_exposicao()
