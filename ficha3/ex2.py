def countText(texto):
    num_caracteres = len(texto)
    
    num_espacos = texto.count(' ')
    
    vogais = "aeiouAEIOU"
    num_vogais = sum(1 for letra in texto if letra in vogais)
    
    print(f"Número de caracteres: {num_caracteres}")
    print(f"Número de espaços: {num_espacos}")
    print(f"Número de vogais: {num_vogais}")

texto = input("Digite um texto: ")

countText(texto)