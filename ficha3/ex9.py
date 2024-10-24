def printCharLine(texto,numeroCar):
    index = 0
    
    while index < len(texto):
        print(texto[index:index + numeroCar])
        
        index += numeroCar

texto = input("Digite o texto: ")
numeroCar = int(input("Digite o número de caracteres por linha: "))

printCharLine(texto, numeroCar)  
    