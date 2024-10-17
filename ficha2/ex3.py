import random
num = random.randint(1,50)
tentativas = 0
tentativasmax = 10

while tentativas < tentativasmax:
    palpite = int(input("Digite o seu palpite: "))
    tentativas += 1  

    if palpite < num:
        print("Número é maior")
    elif palpite > num:
        print("Número é menor")
    else: 
        palpite == num
        print(f"Acertou em {tentativas}") 
 
if tentativas == tentativasmax and palpite != num:
    print(f"Esgotou as {tentativasmax} tentativas :( O número era {num}.")