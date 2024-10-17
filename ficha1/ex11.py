idade =int(input("Idade:"))



if 0 < idade < 2:
    print("Primeira Infancia")
elif 3 < idade < 6:
    print("Infancia Intermedia")
elif 7 < idade < 12:
    print("Pré-Adolescencia")
elif 13 < idade < 19:
    print("Adolescencia")
elif 20 < idade < 59:
    print("Adultez")
elif idade >= 60:
    print("Terceira idade")