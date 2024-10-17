n = int(input("Digite o número de termos da sequência de Fibonacci: "))

a, b = 0, 1

print("Sequência de Fibonacci:")
for _ in range(n):   #_ significa que o valor da variavel nao importa
    print(a, end=' ')
    a, b = b, a + b  
