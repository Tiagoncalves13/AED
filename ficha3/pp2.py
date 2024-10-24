nome_completo = input("Digite o nome completo: ")

primeiro_nome = nome_completo.split()[0]

sobrenome = nome_completo.split()[-1]

print(f"Primeiro nome: {primeiro_nome}")
print(f"Último sobrenome: {sobrenome}")