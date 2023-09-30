import re

# Definindo o código HTML de entrada
entrada_html = """<!DOCTYPE html>
<!-- Isso é um comentário HTML -->
<html>
<head>
    <title>Exemplo de HTML</title>
    <!-- Definindo estilos CSS internamente -->
    <style>
        body {
            background: #f0f0f0;
            color: #333;
            font-size: 16px;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #007acc;
        }
        .container {
            width: 800px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            background: #fff;
        }
    </style>
</head>
<body>
    <div id="conteudo" class="container">
        <h1>Título</h1>
        <p>Este é um exemplo de parágrafo.</p>
        <img src="imagem.jpg" width="300" height="200" style="border: 1px solid #999;">
        <div id="outraDiv" style="background: #ff9900;">
            <span>Este é um span dentro de uma div.</span>
            <br>
            <h2>Subtítulo</h2>
        </div>
    </div>
</body>
</html>
"""

# Usando expressões regulares para encontrar tags HTML
tags = re.findall(r'<(/?\w+)([^>]*)>', entrada_html)

tags_abertura = []
tags_fechamento = []
nivel = 0
linhas = entrada_html.splitlines()
atributos = {}
print("----------------------------------------------------")
print('\033[1m' + "Tags de abertura e fechamento\n" + '\033[0m')
print("----------------------------------------------------")

# Percorrendo cada linha do código HTML
for linha, linha_html in enumerate(linhas, start=1):
    for tag, atributos_str in re.findall(r'<(/?\w+)([^>]*)>', linha_html):
        if '/' not in tag:
            if not tag.endswith('/'):
                print(
                    f"Tag de abertura   : {tag.ljust(9)} | Nível: {nivel} | Linha: {linha}"
                )
                if not tag.lower() in ['br', 'img', 'h']:
                    tags_abertura.append(tag)
                    nivel += 1
        else:
            tag_fechamento = tag[1:]
            if tags_abertura and tags_abertura[-1] == tag_fechamento:
                nivel -= 1
                tags_fechamento.append("Tag de fechamento : " +
                                       str(tag_fechamento.ljust(9)) + " " +
                                       "| Nível : " + str(nivel) + "| Linha: " +
                                       str(linha))
                tags_abertura.pop()
        atributos_str = atributos_str.strip()
        if atributos_str:
            atributos_str = re.findall(r'(\w+)="([^"]*)"', atributos_str)
            for atributo, valor in atributos_str:
                atributos[tag] = atributos.get(tag, {})
                atributos[tag][atributo] = (valor, linha)

print("")
for tag in tags_fechamento:
    print(tag)
print("----------------------------------------------------")
print('\033[1m' + "Atributos de cada tag" + '\033[0m')
print("----------------------------------------------------")

# Imprimindo os atributos de cada tag HTML
for tag, atributo_valor in atributos.items():
    print(f"Tag: {tag}\n")
    for atributo, (valor, linha_atributo) in atributo_valor.items():
        print(f"• Atributo: {atributo.ljust(18)} | Linha: {linha_atributo}")
        print(f"• Valor do Atributo: {valor}\n")
    print("")

# Encontrando as regras de estilo CSS dentro da tag <style>
style_tag = re.search(r'<style>(.*?)</style>', entrada_html, re.DOTALL)
if style_tag:
    css_content = style_tag.group(1)
    css_rules = re.findall(r'([a-zA-Z0-9\s,.#\-]+)\s*{([^}]*)}', css_content)
    print("----------------------------------------------------")
    print('\033[0m' + "Seletores Dentro da tag style" + '\033[0m')
    print("----------------------------------------------------")

    # Imprimindo as regras de estilo CSS
    for selector, properties in css_rules:
        print("")
        print(f"Seletor: {selector.strip()}\n")
        properties = properties.strip()
        css_properties = re.findall(r'([a-zA-Z-]+)\s*:\s*([^;]+);', properties)
        for property_name, property_value in css_properties:
            print(f"  • Atributo: {property_name.strip()}")
            print(f"  • Valor do Atributo: {property_value.strip()}\n")

