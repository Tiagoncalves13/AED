def somatorio(num1, num2):

    soma = 0
    for i in range(num1, num2 + 1):
        soma += i

    print(f"O somatório de {num1} até {num2} é: {soma}")

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

somatorio(num1, num2)
    


    
    