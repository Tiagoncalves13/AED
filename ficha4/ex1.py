def acima_da_media(numeros):
    media = sum(numeros) / len(numeros)
    contador = 0
    for numero in numeros:
        if numero > media:
            contador += 1
    return contador

numeros = []
for _ in range(10):
    numero = int(input("Insira um número inteiro: "))
    numeros.append(numero)

resultado = acima_da_media(numeros)
print("Números acima da média:", resultado)
