from PIL import Image
import os

def ImageArt():
    # Definir tamanho da imagem e criar uma imagem RGB vazia
    largura, altura = 400, 400
    imagem = Image.new("RGB", (largura, altura))

    # Preencher a imagem com valores RGB aleatórios
    for x in range(largura):
        for y in range(altura):
            # Gera valores aleatórios para R, G, B entre 0 e 255
            r = x % 256  # Apenas para exemplo, substitua por valores aleatórios reais
            g = y % 256
            b = (x + y) % 256
            imagem.putpixel((x, y), (r, g, b))

    # Certifique-se de que a pasta "images" existe
    if not os.path.exists("images"):
        os.makedirs("images")
    
    # Salvar a imagem na pasta "images" com o nome "imageArt.jpg"
    imagem.save("images/imageArt.jpg")
    imagem.show()

# Chamar a função para criar e salvar a imagem
ImageArt()
