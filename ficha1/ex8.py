sexo = str(input("Qual o seu sexo (F/M): "))
altura = int(input("Digite a sua altura: "))

if sexo == ("F"):
    pesoid = (altura - 100) - (altura - 150) / 2
    print("Peso ideal: {:.2f}" .format(pesoid))

elif sexo == ("M"):
    pesoid = (altura - 100) - (altura - 150) / 4
    print("Peso ideal: {:.2f} kg" .format(pesoid))

else: 
     print("Introduza valores corretos")