def removeSpaces(texto):
    palavras = texto.split()
    
    texto_resultante = ' '.join(palavras)
    
    print(texto_resultante)

texto = input("Digite um texto: ")

removeSpaces(texto)
