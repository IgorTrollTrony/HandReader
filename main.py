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
    largura = estilo.get('width', '')
    altura = estilo.get('height', '')
    return largura, altura

# HTML de entrada
entrada_html = """
<html> 
  <head>
    <title> Compiladores </title>
  </head>
  <body> 
    <p style="color:red;background:blue" id="abc"> Unipinhal </p>
    <div style="color: red;background:blue; width: 300px; height: 50px;" id="abc"> asdadada </div>
    <div style="color: red;background:blue; width: 200px; height: 200px;" id="abc"> asdadada </div>
    <br></br>
    <p style="color:red;background:blue" id="abc"> Unipinhal </p>
    <br>
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
    tags_com_estilo = re.findall(r'<([a-zA-Z0-9]+)[^>]style="([^"])"[^>]>(.?)</?\1>', html)

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

            if tag.lower() == 'br':  # Verifica se a tag é <br> (case-insensitive)
                largura, altura = '0px', '36px'  # Define largura e altura padrão para a tag br
            else:
                largura, altura = extrair_largura_e_altura(estilo_dict)

            # Verifica se largura e altura não estão vazias
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

            altura_div_anterior = tamanho_elemento[1]
            y += altura_div_anterior + espacamento_vertical  # Adiciona espaçamento vertical após a div

        pygame.display.update()

    # Finaliza o Pygame
    pygame.quit()

# Chame a função para processar o HTML e exibir o conteúdo de todas as tags com conteúdo
espacamento_horizontal = 20
espacamento_vertical = 0  # Espaçamento de 36px para a tag <br>
processar_html_pygame(entrada_html, espacamento_horizontal, espacamento_vertical)
