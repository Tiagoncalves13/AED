soma = 0
i = 0
maior_numero = 0  

while i < 10:
    numero = int(input("Indique o {:n}º numero: ".format(i + 1)))
    if numero > 20:
        continue
    soma += numero
   
    if numero > maior_numero:
        maior_numero = numero 
   
    i += 1


media = soma / (i if i > 0 else 1)

print("A média é {:n}".format(media))
print("O maior número é {:n}".format(maior_numero))
