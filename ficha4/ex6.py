def searchNumber(lista, pesquisa):
    posicoes = [i for i, num in enumerate(lista) if num == pesquisa]
    return posicoes

# Coleta de 10 números inteiros
lista = []
print("Insira 10 números inteiros:")
for i in range(10):
    numero = int(input(f"Número {i + 1}: "))
    lista.append(numero)

# Solicita o valor de pesquisa
valor_pesquisa = int(input("Digite o valor que deseja pesquisar: "))

# Chama a função de busca
posicoes_encontradas = searchNumber(lista, valor_pesquisa)

# Exibe o resultado
if posicoes_encontradas:
    print(f"O valor {valor_pesquisa} foi encontrado nas posições: {posicoes_encontradas}.")
else:
    print(f"O valor {valor_pesquisa} não foi encontrado na lista.")
