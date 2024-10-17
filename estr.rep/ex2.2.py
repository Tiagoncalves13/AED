numero = int(input("Digite um número: "))
fatorial = 1
n = numero

while n > 1:
    fatorial *= n
    n -= 1

print(f"Fatorial de {numero} = {fatorial}")
