def positiveList(pontuacoes, nomes):
    # Cria listas para as pontuações e nomes positivos
    pontuacoes_positivas = []
    nomes_positivos = []
    
    for i in range(len(pontuacoes)):
        if pontuacoes[i] >= 10:
            pontuacoes_positivas.append(pontuacoes[i])
            nomes_positivos.append(nomes[i])
    
    return pontuacoes_positivas, nomes_positivos

# Coleta de pontuações e nomes
pontuacoes = []
nomes = []

for i in range(10):
    nome = input(f"Nome do participante {i + 1}: ")
    
    while True:
        try:
            pontuacao = float(input(f"Pontuação do participante {nome} (0 a 20): "))
            if 0 <= pontuacao <= 20:
                pontuacoes.append(pontuacao)
                nomes.append(nome)
                break
            else:
                print("Pontuação inválida! Deve estar entre 0 e 20.")
        except ValueError:
            print("Entrada inválida! Insira um número.")

# Exibe as pontuações e nomes positivos
pontuacoes_positivas, nomes_positivos = positiveList(pontuacoes, nomes)
print("Pontuações positivas (>= 10):", pontuacoes_positivas)
print("Nomes dos participantes com pontuações positivas:", nomes_positivos)
