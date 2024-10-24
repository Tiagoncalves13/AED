def shortName(nome):
    partes = nome.split()
    
    primeiro_nome = partes[0]
    ultimo_sobrenome = partes[-1]
    
    return f"{primeiro_nome} {ultimo_sobrenome}"

nome = input("Digite o nome completo: ")

resultado = shortName(nome)
print(resultado)
