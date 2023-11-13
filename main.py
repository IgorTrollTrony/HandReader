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

import pygame
import re

# Função para extrair o estilo
def extrair_estilo(style):
    estilo = {}
    for prop in style.split(';'):
        prop = prop.strip()
        if prop:
            nome, valor = prop.split(':')
            estilo[nome.strip()] = valor.strip()
    return estilo

# Função para extrair o valor da largura (width) e altura (height) do estilo
def extrair_largura_e_altura(estilo):
    largura = estilo.get('width')
    altura = estilo.get('height')
    return largura, altura

# HTML de entrada
entrada_html = """
<html> 
  <head>
    <title> Compiladores </title>
  </head>
  <body> 
    <p style="color:red;background:blue" id="abc"> Unipinhal </p>
    <div style="color: red;background:blue; width: 200px; height: 50px;" id="abc"> asdadada </div>
    <div style="color: red;background:blue; width: 200px; height: 200px;" id="abc"> asdadada </div>
    <p style="color:red;background:blue" id="abc"> Unipinhal </p>
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

    # Encontre o conteúdo de todas as tags com conteúdo e seus estilos
    tags_com_estilo = re.findall(r'<([a-zA-Z0-9]+)[^>]style="([^"]+)"[^>]>(.*?)</\1>', html)

    # Inicialize a altura da div anterior
    altura_div_anterior = 0

    # Loop principal do Pygame
    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        janela.fill((255, 255, 255))  # Preencher a janela com branco

        y = 0

        for tag, estilo, conteudo in tags_com_estilo:
            x = espacamento_horizontal  # Defina a posição x como desejar
            estilo_dict = extrair_estilo(estilo)

            largura, altura = extrair_largura_e_altura(estilo_dict)
            if largura and altura:
                tamanho_elemento = (int(largura.rstrip('px')), int(altura.rstrip('px')))
            else:
                tamanho_texto = fonte.size(conteudo)
                tamanho_elemento = tamanho_texto

            # Renderiza o fundo com base no tamanho do elemento
            cor_de_fundo = pygame.Color(estilo_dict.get('background', 'white'))
            fundo = pygame.Surface(tamanho_elemento)
            fundo.fill(cor_de_fundo)
            janela.blit(fundo, (x, y))

            cor = estilo_dict.get('color', 'black')
            cor_texto = pygame.Color(cor)
            texto = fonte.render(conteudo, True, cor_texto)
            janela.blit(texto, (x, y))

            # Atualiza a altura da div anterior
            altura_div_anterior = tamanho_elemento[1]

            if tag == 'br':
                y += espacamento_vertical  # Aplica o espaçamento apenas para a tag <br>
            else:
                y += altura_div_anterior

        pygame.display.update()

    # Finaliza o Pygame
    pygame.quit()

# Chame a função para processar o HTML e exibir o conteúdo de todas as tags com conteúdo
espacamento_horizontal = 20
espacamento_vertical = 36  # Espaçamento de 36px para a tag <br>
processar_html_pygame(entrada_html, espacamento_horizontal, espacamento_vertical)