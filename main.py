import pygame
import re

# HTML de entrada
entrada_html = """
<html>
<head>
   <title>replit</title>
 </head>
<body>
  <p>Hello world</p>
  <h1 style="font-size:30px;">Olá, Eu sou uma página </h1>
  <div id="teste" style="color:black;">Unipinhal</div>
  <div id="teste" style="color:black;">Unipinhal</div>
  <div id="teste" style="color:black;">Unipinhal</div>
</body>
</html>
"""

def processar_html_pygame(html, espacamento_horizontal, espacamento_vertical):
    # Inicialização do Pygame
    pygame.init()

    # Configuração da janela
    largura = 800
    altura = 600
    janela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Navegador Web")

    # Configuração de fonte
    fonte = pygame.font.Font(None, 36)
    cor_texto = (0, 0, 0)  # Cor preta

    # Encontre o conteúdo de todas as tags com conteúdo
    conteudo_tags = re.findall(r'<([a-zA-Z0-9]+)[^>]*>(.*?)</\1>', html)

    # Loop principal do Pygame
    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        janela.fill((255, 255, 255))  # Preencher a janela com branco

        y = espacamento_vertical
        for tag, conteudo in conteudo_tags:
            x = espacamento_horizontal  # Defina a posição x como desejar
            texto = fonte.render(conteudo, True, cor_texto)
            janela.blit(texto, (x, y))
            y += espacamento_vertical

        pygame.display.update()

    # Finaliza o Pygame
    pygame.quit()

# Chame a função para processar o HTML e exibir o conteúdo de todas as tags com conteúdo
espacamento_horizontal = 20
espacamento_vertical = 30
processar_html_pygame(entrada_html, espacamento_horizontal, espacamento_vertical)
