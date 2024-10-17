# Lê um número entre 1 e 99
numero = int(input("Digite um número entre 1 e 99: "))

# Verifica se o número está dentro do intervalo
if 1 <= numero <= 99:
    representacao_binaria = ""
    
    # Converte o número para binário manualmente
    while numero > 0:
        resto = numero % 2  # Obtém o resto da divisão por 2
        representacao_binaria = str(resto) + representacao_binaria  # Concatena o resto na frente
        numero = numero // 2  # Divide o número por 2
    
    # Imprime a representação em binário com espaços
    print(f"Resultado: {representacao_binaria}")
else:
    print("Por favor, digite um número válido entre 1 e 99.")
