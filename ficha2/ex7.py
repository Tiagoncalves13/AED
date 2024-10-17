number = int(input("Digite um número inteiro e positivo: "))

if number < 1:
    print("Por favor, digite um número positivo.")
else:
    divisors_sum = 0
    
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i

    if divisors_sum == number:
        print(f"{number} é um número perfeito.")
    else:
        print(f"{number} não é um número perfeito.")
