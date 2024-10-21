n = int(input("Digite a quantidade de números que você deseja inserir: "))

maior = 0
segundo_maior = 0

for i in range(n):
    numero = int(input(f"Digite o número {i + 1}: "))
    
    if numero > maior:
        segundo_maior = maior  
        maior = numero
    elif numero > segundo_maior:
        segundo_maior = numero


print(f"O segundo maior valor é: {segundo_maior}")
