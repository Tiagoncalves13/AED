def romanNumeral(num):
    # Dicionário para mapear números a seus equivalentes romanos
    valores = [
        (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    # Verifica se o número está dentro do intervalo permitido
    if num < 1 or num > 999:
        return "Número fora do intervalo permitido (1 a 999)."
    
    resultado = ''
    
    # Constrói a representação romana
    for valor, simbolo in valores:
        while num >= valor:
            resultado += simbolo
            num -= valor
    
    return resultado

# Solicita um número ao usuário
numero = int(input("Digite um número entre 1 e 999: "))

# Chama a função e imprime o resultado
resultado = romanNumeral(numero)
print(resultado)
