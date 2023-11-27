# Importa as bibliotecas necessárias
import pygame  # Biblioteca para desenvolvimento de jogos em Python
import re  # Módulo para trabalhar com expressões regulares

# Função para extrair o estilo de uma string CSS e retornar um dicionário
def extrair_estilo(style):
    estilo = {}
    # Itera sobre as propriedades de estilo separadas por ';'
    for prop in style.split(';'):
        prop = prop.strip()
        if prop:
            # Divide a propriedade em nome e valor e armazena no dicionário
            nome, valor = prop.split(':')
            estilo[nome.strip()] = valor.strip()
    return estilo

# Função para extrair a largura e altura de um dicionário de estilo
def extrair_largura_e_altura(estilo):
    largura = estilo.get('width', '')
    altura = estilo.get('height', '')
    return largura, altura

# Função principal para processar o HTML e exibir o conteúdo no Pygame
def processar_html_pygame(html, espacamento_horizontal, espacamento_vertical):
    # Inicializa o Pygame
    pygame.init()

    # Configuração da janela
    largura = 800
    altura = 600
    janela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Navegador Web")
    fonte = pygame.font.Font(None, 36)

    # Encontra todas as tags com estilo no HTML usando expressões regulares
    tags_com_estilo = re.findall(r'<([a-zA-Z0-9]+)[^>]*style="([^"]+)"[^>]*>(.*?)</?\1>|<br[^>]*>', html)

    # Loop principal do Pygame
    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        # Preenche a janela com branco
        janela.fill((255, 255, 255))

        y = 0

        # Loop através de todas as tags com estilo
        for tag, estilo, conteudo in tags_com_estilo:
            x = espacamento_horizontal
            estilo_dict = extrair_estilo(estilo)

            # Verifica se a tag é <br> (quebra de linha)
            if tag.lower() == 'br':
                largura, altura = '200px', '200px'
            else:
                largura, altura = extrair_largura_e_altura(estilo_dict)

            # Verifica se largura e altura não estão vazias
            if largura and altura:
                tamanho_elemento = (int(largura.rstrip('px')), int(altura.rstrip('px')))
            else:
                # Se não houver largura e altura especificadas, usa o tamanho do texto
                tamanho_texto = fonte.size(conteudo)
                tamanho_elemento = tamanho_texto

            # Renderiza o fundo com base no tamanho do elemento
            cor_de_fundo = pygame.Color(estilo_dict.get('background', 'white'))
            fundo = pygame.Surface(tamanho_elemento)
            fundo.fill(cor_de_fundo)
            janela.blit(fundo, (x, y))

            # Renderiza o texto na janela
            cor = estilo_dict.get('color', 'black')
            cor_texto = pygame.Color(cor)
            texto = fonte.render(conteudo, True, cor_texto)
            janela.blit(texto, (x, y))

            # Atualiza a posição y considerando o tamanho do elemento e o espaçamento vertical
            y += tamanho_elemento[1] + espacamento_vertical

        # Atualiza a janela do Pygame
        pygame.display.update()

    # Finaliza o Pygame
    pygame.quit()

# HTML de entrada
entrada_html = """
<html> 
  <head>
    <title> Compiladores </title>
  </head>
  <body> 
    <p style="color:White;background:Black" id="abc"> Bem vindo </p>
    <br>
    <div style="color: white;background:Black; width: 1920px; height: 50px;" id="abc"> Mini Compilador </div>
    <div style="color: red;background:blue; width: 250px; height: 200px;" id="abc"> apresentação teste </div>
    <br>
    <p style="color:White;background:Black" id="abc"> Unipinhal </p>
  </body>
</html>
"""

# Parâmetros para espaçamento horizontal e vertical
espacamento_horizontal = 20
espacamento_vertical = 0

# Chama a função principal para processar o HTML e exibir o conteúdo
processar_html_pygame(entrada_html, espacamento_horizontal, espacamento_vertical)
