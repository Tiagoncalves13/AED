def maior(*numeros):
      
    
    maior_numero = numeros[0]
    
    
    for num in numeros[1:]:
        if num > maior_numero:
            maior_numero = num
    
    return maior_numero

resultado = maior(10, 20, 35, 7, 89, 3)
print(f"O maior número é: {resultado}")