
numero = int(input("Digite um número: "))

primo = True
for i in range(2, numero):
    resto = numero % i
    if resto == 0:
        primo = False
        break
if primo == True:
    print("O número é primo")
else:
     print("O número não é primo")



