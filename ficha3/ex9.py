def printCharLine(texto,numeroCar):
    index = 0
    
    while (len(texto) > numCar):
        print(texto[0:numeroCar])
        texto=texto[numCar:]
        print(texto)

texto = input("Digite o texto: ")
numeroCar = int(input("Digite o número de caracteres por linha: "))

printCharLine(texto, numeroCar)  
    