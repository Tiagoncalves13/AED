def printCharLine(texto, numeroCar):
    index = 0
    
    while index < len(texto):
        print(texto[index:index + numeroCar])
        index += numeroCar

texto = input("Digite o texto: ")

while True:
    try:
        numeroCar = int(input("Digite o número de caracteres por linha (entre 5 e 12): "))
        
        if 5 <= numeroCar <= 12:
            break  
        else:
            print("Por favor, insira um número entre 5 e 12.")
            
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro entre 5 e 12.")

printCharLine(texto, numeroCar)
