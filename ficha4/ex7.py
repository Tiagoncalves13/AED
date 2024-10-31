def pluviosidade(pluviosidade):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    # Combina meses com pluviosidade e ordena
    dados = sorted(zip(meses, pluviosidade), key=lambda x: x[1], reverse=True)

    # Imprime os dados ordenados
    print("\nPluviosidade mensal (ordem decrescente):")
    for mes, valor in dados:
        print(f"{mes}: {valor:.2f} mm")

# Coleta de pluviosidade mensal
pluviosidade_mensal = []
print("Insira a pluviosidade (em mm) para cada mês:")

for mes in [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]:
    valor = float(input(f"{mes}: "))  # Lê o valor da pluviosidade
    pluviosidade_mensal.append(valor)  # Adiciona à lista

# Chama a função para imprimir os dados
pluviosidade(pluviosidade_mensal)

#corrigir soluçao