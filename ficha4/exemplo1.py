# Lista de cidades
cidades = ['Porto', 'Maia', 'Matosinhos', 'Vila do Conde', 'Póvoa de Varzim', 'Gondomar', 'Gaia']

# Função para calcular a estatística
def dados_estatistica(temperaturas):
    # Calcula a média das temperaturas
    media = sum(temperaturas) / len(temperaturas)
    
    # Inicializa as variáveis para armazenar a maior distância da média e a cidade correspondente
    maior_diferenca = 0
    cidade_mais_distante = ""
    
    # Encontra a temperatura mais distante da média e a cidade correspondente
    for i in range(len(temperaturas)):
        diferenca = temperaturas[i] - media
        # Converte a diferença para valor positivo sem usar abs()
        if diferenca < 0:
            diferenca = -diferenca  # Se for negativa, torna-a positiva
        
        # Atualiza se essa diferença for a maior encontrada
        if diferenca > maior_diferenca:
            maior_diferenca = diferenca
            cidade_mais_distante = cidades[i]
    
    return cidade_mais_distante, maior_diferenca

# Função principal para ler as temperaturas e validar os dados
def main():
    temperaturas = []
    
    for cidade in cidades:
        while True:
            try:
                # Lê a temperatura da cidade
                temp = float(input(f"Introduza a temperatura em {cidade} (entre 0 e 40): "))
                
                # Valida o intervalo da temperatura
                if 0 <= temp <= 40:
                    temperaturas.append(temp)
                    break
                else:
                    print("Por favor, insira uma temperatura entre 0 e 40.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")
    
    # Calcula e mostra o resultado da estatística
    cidade_mais_distante, diferenca = dados_estatistica(temperaturas)
    print(f"A temperatura mais distante da média ocorreu em {cidade_mais_distante}, com uma diferença de {diferenca:.2f} graus.")
    
# Executa o programa principal
main()
