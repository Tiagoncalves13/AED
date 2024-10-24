def capicua(texto):
    return texto == texto[::-1]

texto = input("Digite um texto: ")

if capicua(texto):
    print("O texto inserido é uma capicua.")
else:
    print("O texto inserido não é uma capicua.")
