def printCharLine(texto,numeroCar):
    
    
    while (len(texto) > numeroCar):
        print(texto[0:numeroCar])
        texto=texto[numeroCar:]
        print(texto)

texto = input("Digite o texto: ")
numeroCar = int(input("Digite o número de caracteres por linha: "))

printCharLine(texto, numeroCar)  
    