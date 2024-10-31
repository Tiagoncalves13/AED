import random

def generateNumbers(limite_inferior, limite_superior, quantidade):
    return random.sample(range(limite_inferior, limite_superior + 1), quantidade)

while True:
    numeros = generateNumbers(1, 50, 5)  # 5 números entre 1 e 50
    estrelas = generateNumbers(1, 12, 2)  # 2 estrelas entre 1 e 12
    
    print("Chave do Euromilhões:")
    print("Números:", sorted(numeros))  # Exibe os números em ordem
    print("Estrelas:", sorted(estrelas))  # Exibe as estrelas em ordem
    
    resposta = input("Deseja gerar nova chave? (S/N): ").strip().upper()
    if resposta != 'S':
        break
