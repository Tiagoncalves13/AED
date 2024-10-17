sexo = str(input("Qual o seu sexo (F/M): "))
idade = int(input("Digite a sua idade: "))

calcf = (226 - idade )
calcm = (220 - idade )

if sexo == ("F"):
    print(f'FCM: {calcf} ')

elif sexo ==("M"):
    print(f'FCM: {calcm} ')

else:
    print("Introduza valores corretos")
 

