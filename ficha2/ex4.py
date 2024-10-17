import random

while True: #criacao de um loop infinito
    num = random.randint(1, 50)
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
            print(f"Acertou em {tentativas} tentativas!") 
            break  

    if tentativas == tentativasmax and palpite != num:
        print(f"Esgotou as {tentativasmax} tentativas :( O número era {num}.")

    resposta = input("\nNovo jogo (S/N)? ")

    match resposta:
        case 'S':
            continue  
        case 'N':
            print("Obrigado por jogar! Até a próxima!")
            break  
        case _:
            print("Opção inválida! Saindo do jogo.")
            break  


    
    
    