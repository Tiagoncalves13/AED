def reverseWords(texto):
    palavras = texto.split()
    
    palavras_invertidas = palavras[::-1]
    
    texto_invertido = ' '.join(palavras_invertidas)
    
    return texto_invertido

texto = input("Digite um texto: ")

resultado = reverseWords(texto)
print(resultado)
