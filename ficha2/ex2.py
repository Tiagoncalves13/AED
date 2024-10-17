inf = int(input("Digite o limite inferior: "))
sup = int(input("Digite o limite superior: "))

soma = 0


for numero in range(inf, sup + 1):
    if numero % 2 == 0:  # Verificar se o número é par
        soma += numero   # Adição acumulada(soma o valor à direita dele ao valor da variável à esquerda)


print(f"A soma de todos os pares entre {inf} e {sup} é {soma}")

