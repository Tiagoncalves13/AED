def ordenar_sem_duplicados(lista):
    # Ordena a lista e remove duplicatas usando set
    lista_ordenada = sorted(set(lista))
    return lista_ordenada

# Pede o número de elementos da lista
N = int(input("Digite o número de elementos da lista: "))

# Coleta os elementos da lista
lista = []
for i in range(N):
    valor = int(input(f"Elemento {i + 1}: "))
    lista.append(valor)

# Chama a função para ordenar e remover duplicados
lista_final = ordenar_sem_duplicados(lista)

# Exibe a lista gerada
print("Lista gerada:", lista_final)
