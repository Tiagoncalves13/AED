def standardName(nome):
    partes = nome.split()
    
    primeiro_nome = partes[0]
    
    ultimo_sobrenome = partes[-1]
    
    iniciais = []
    
    for parte in partes[1:-1]:
        iniciais.append(parte[0] + '.')
    
    nome_normalizado = f"{primeiro_nome} {' '.join(iniciais)} {ultimo_sobrenome}"
    
    return nome_normalizado

nome = input("Digite o nome completo: ")

resultado = standardName(nome)
print(resultado)
