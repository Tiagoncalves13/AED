cidades = ['Porto', 'Maia', 'Matosinhos', 'Vila do Conde', 'Póvoa de Varzim', 'Gondomar', 'Gaia']

def dadosEstatistica(temperaturas):
    
    media = sum(temperaturas) / len(temperaturas)

    maior_dif = 0
    cidade_m_distante = ""

    for i in range(len(temperaturas)):
        diferenca = temperaturas[i] - media
        if diferenca > maior_dif:
            maior_dif = diferenca
            cidade_m_distante = cidades[i]
    return cidade_m_distante, maior_dif

def principal():
    temperaturas = []

    for cidade in cidades:
        while True:
            try:
                temp = int(input(f"Temperatura na cidade {cidades} (valor entre 0 e 40ºC)"))
                if 0 <= temp <= 40:
                    temperatura.append(temp) 
                    break
                else:
                    print("O valor da temperatura não está de acordo com os limites ")
            except ValueError:
             print("Apenas pode inserir numeros")
            cidade_m_distante, diferenca = dados_estatistica(temperaturas)
            print(f"A temperatura é maior em {cidade_m_distante}")
principal()


    

            
