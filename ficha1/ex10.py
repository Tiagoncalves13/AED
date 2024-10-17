print(" Planetas")
print("\n 1- Mercurio")
print(" 2- Venus")
print(" 3- Marte")
print(" 4- Júpiter")
print(" 5- Saturno")
print(" 6- Urano")

peso =float(input("Peso:"))
codplan = input("Codigo do Planeta (1-6)")
match codplan:
    case "1":
        pesoplan = (peso * 0.37) / 0.98
        print("O seu peso no planeta 1 é {:.2f} kg" .format(pesoplan))
    case "2":
        pesoplan = (peso * 0.90) / 0.98
        print("O seu peso no planeta 2 é {:.2f} kg" .format(pesoplan))
    case "3":
        pesoplan = (peso * 0.37) / 0.98
        print("O seu peso no planeta 3 é {:.2f} kg" .format(pesoplan))
    case "4":
        pesoplan = (peso * 2.53) / 0.98
        print("O seu peso no planeta 4 é {:.2f} kg" .format(pesoplan))
    case "5":
        pesoplan = (peso * 1.06) / 0.98
        print("O seu peso no planeta 5 é {:.2f} kg" .format(pesoplan))
    case "6":
        pesoplan = (peso * 0.91) / 0.98
        print("O seu peso no planeta 6 é {:.2f} kg" .format(pesoplan))
