# Leitura da matriz 3x3
matriz = []
print("Digite os elementos da matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        elemento = int(input(f"Elemento [{i+1}, {j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

# Impressão da matriz original
print("\nMatriz Original:")
for linha in matriz:
    print(linha)

# Construção e impressão da matriz transposta
print("\nMatriz Transposta:")
for i in range(3):
    linha_transposta = []
    for j in range(3):
        linha_transposta.append(matriz[j][i])
    print(linha_transposta)
