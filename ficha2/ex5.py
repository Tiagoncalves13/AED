
number = int(input("Digite um número inteiro e positivo: "))


if number < 2:
    print(f"{number} não é um número primo.")
else:
    i = 2
    while i * i <= number:  
        if number % i == 0:
            print(f"{number} não é um número primo.")
            break
        i += 1
    else:
        print(f"{number} é um número primo.")

        #Solução correta mas fiquei sem perceber. Verificar resolução moodle
