altura =float(input("Altura:"))
peso =float(input("Peso:"))
imc = peso / (altura*altura)

print("imc {:.2f}" .format(imc))

if imc < 18.5:
    print("Baixo Peso")
elif 18.5 < imc < 24.9:
    print("Peso Normal")
elif 25 < imc < 29.9:
    print("Excesso de Peso")
elif 30 < imc < 34.9:
    print("Obesidade Grau 1")
elif 35 < imc < 39.9:
    print("Obesidade Grau 2")
elif imc >= 40:
    print("Obesidade Morbida")