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

    # Expressões regulares para encontrar tags e atributos
    tags = re.findall(r'<(/?\w+)([^>]*)>', html)

    tags_info = []
    nivel = 0
    linhas = html.splitlines()
    atributos = []

    # Processamento das tags
    for linha, linha_html in enumerate(linhas, start=1):
        for tag, atributos_str in re.findall(r'<(/?\w+)([^>]*)>', linha_html):
            if '/' not in tag:
                if not tag.endswith('/'):
                    if not tag.lower() in ['br', 'img', 'h', 'input', 'meta']:
                        tags_info.append((tag, "abertura", nivel, linha))
                        nivel += 1
            else:
                tag_fechamento = tag[1:]
                nivel -= 1
                tags_info.append((tag_fechamento, "fechamento", nivel, linha))

            atributos_str = atributos_str.strip()
            if atributos_str:
                atributos_str = re.findall(r'(\w+)="([^"]*)"', atributos_str)
                atributos.extend([(tag, atributo, valor) for atributo, valor in atributos_str])

    # Encontre o conteúdo das tags de texto
    conteudo_tags_texto = []
    for tag_info in tags_info:
        tag, tipo, nivel, linha = tag_info
        if tipo == "abertura":
            if tag in ["p", "h1", "h2", "h3", "h4", "span", "a", "strong", "b", "em", "i", "u", "s", "del", "ins", "mark", "abbr", "cite", "code", "pre"]:
                regex = f'<{tag}[^>]*>(.*?)</{tag}>'
                tags_encontradas = re.findall(regex, linhas[linha - 1], re.DOTALL)
                for conteudo in tags_encontradas:
                    if conteudo.strip():  # Verifique se há conteúdo
                        conteudo_tags_texto.append((tag, conteudo.strip(), linha))

    # Loop principal do Pygame
    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        janela.fill((255, 255, 255))  # Preencher a janela com branco

        for tag_info in tags_info:
            tag, tipo, nivel, linha = tag_info
            x = nivel * espacamento_horizontal
            y = linha * espacamento_vertical
            if tipo == "abertura":
                tag_renderizada = f"<{tag}>"
            else:
                tag_renderizada = f"</{tag}>"
            texto = fonte.render(tag_renderizada, True, cor_texto)
            janela.blit(texto, (x, y))

        for tag, conteudo, linha in conteudo_tags_texto:
            x = espacamento_horizontal  # Defina a posição x como desejar
            y = linha * espacamento_vertical
            texto = fonte.render(conteudo, True, cor_texto)
            janela.blit(texto, (x, y))

        pygame.display.update()

    # Finaliza o Pygame
    pygame.quit()

# Chame a função para processar o HTML e exibi-lo no Pygame
espacamento_horizontal = 20
espacamento_vertical = 30
processar_html_pygame(entrada_html, espacamento_horizontal, espacamento_vertical)
