def positiveList(pontuacoes):
    return [p for p in pontuacoes if p >= 10]

# Coleta de pontuações
pontuacoes = []
for i in range(10):
    while True:
        try:
            pontuacao = float(input(f"Pontuação do participante {i + 1} (0 a 20): "))
            if 0 <= pontuacao <= 20:
                pontuacoes.append(pontuacao)
                break
            else:
                print("Pontuação inválida! Deve estar entre 0 e 20.")
        except ValueError:
            print("Entrada inválida! Insira um número.")

# Exibe as pontuações positivas
pontuacoes_positivas = positiveList(pontuacoes)
print("Pontuações positivas (>= 10):", pontuacoes_positivas)
