def countWord(texto, palavra):
    contador = 0
    posicoes = []

    palavras = texto.split()

    for i, p in enumerate(palavras):
        if p == palavra:
            contador += 1
            posicoes.append(i)

    return contador, posicoes

texto = input("Digite o texto: ")
palavra = input("Digite a palavra para pesquisar: ")

contador, posicoes = countWord(texto, palavra)
print(f"A palavra '{palavra}' ocorre {contador} vez(es) nas posições: {posicoes}")
