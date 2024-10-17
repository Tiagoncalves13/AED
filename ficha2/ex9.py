n = int(input("Digite a quantidade de números que você deseja inserir: "))

maior = None
segundo_maior = None

for i in range(n):
    numero = int(input(f"Digite o número {i + 1}: "))
    
    if maior is None or numero > maior:
        segundo_maior = maior  
        maior = numero
    elif segundo_maior is None or (numero > segundo_maior and numero != maior):
        segundo_maior = numero

if segundo_maior is not None:
    print(f"O segundo maior valor é: {segundo_maior}")
else:
    print("Não foi possível determinar o segundo maior valor.")
