def faturacao_empresa():
    faturacao = []
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    # Coleta de faturação mensal
    print("Insira a faturação mensal da empresa:")
    for mes in meses:
        valor = float(input(f"{mes}: "))
        faturacao.append(valor)

    # Cálculos
    mes_maior = meses[faturacao.index(max(faturacao))]
    mes_menor = meses[faturacao.index(min(faturacao))]
    media = sum(faturacao) / len(faturacao)

    # Exibição dos resultados
    print(f"\nMês de maior faturação: {mes_maior} com {max(faturacao):.2f} unidades.")
    print(f"Mês de menor faturação: {mes_menor} com {min(faturacao):.2f} unidades.")
    print(f"Média mensal de faturação: {media:.2f} unidades.")

# Executa o programa
faturacao_empresa()
