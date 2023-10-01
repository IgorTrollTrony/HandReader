import re

entrada_html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exemplo de HTML e CSS</title>
    <style>
        /* Estilos para o corpo da página */
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }

        /* Estilos para o cabeçalho */
        header {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 20px;
        }

        /* Estilos para as divs */
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
            margin-top: 20px;
        }

        /* Estilos para os botões */
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 3px;
        }

        /* Estilos para links */
        a {
            color: #007bff;
            text-decoration: none;
        }

        /* Estilos para a barra de navegação */
        nav {
            background-color: #333;
            color: #fff;
            padding: 10px;
        }

        /* Estilos para rodapé */
        footer {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Meu Site</h1>
    </header>
    <nav>
        <ul>
            <li><a href="#">Página Inicial</a></li>
            <li><a href="#">Sobre Nós</a></li>
            <li><a href="#">Contato</a></li>
        </ul>
    </nav>
    <div class="container">
        <h2>Bem-vindo ao nosso site</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis libero a hendrerit. Vestibulum dapibus, justo vel fringilla vehicula, quam arcu elementum ex.</p>
        <a href="#" class="btn">Saiba mais</a>
    </div>
    <div class="container">
        <h2>Nossos Serviços</h2>
        <ul>
            <li>Serviço 1</li>
            <li>Serviço 2</li>
            <li>Serviço 3</li>
        </ul>
    </div>
    <footer>
        &copy; 2023 Meu Site
    </footer>
</body>
</html>

"""

#/? pode ou ter /
#\w+ um ou mais caracteres de palavra
tags = re.findall(r'<(/?\w+)([^>]*)>', entrada_html)

tags_abertura = []
tags_fechamento = []
nivel = 0
linhas = entrada_html.splitlines()
atributos = {}


# Encontre o DOCTYPE
doctype_match = re.search(r'<!DOCTYPE\s+([^>]+)>', entrada_html)
if doctype_match:
    print("----------------------------------------------------")
    doctype = doctype_match.group(1)
    print(f"DOCTYPE: {doctype.strip()}")

# Encontre a declaração de codificação UTF
encoding_match = re.search(r'<meta\s+charset=["\']?([^"\']+)["\']?\s*/?>', entrada_html)
if encoding_match:
    encoding = encoding_match.group(1)
    print(f"Codificação UTF: {encoding.strip()}")

print("----------------------------------------------------")
print('\033[1m' + "Tags de abertura e fechamento\n" + '\033[0m')
print("----------------------------------------------------")
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
for tag, atributo_valor in atributos.items():
    print(f"Tag: {tag}\n")
    for atributo, (valor, linha_atributo) in atributo_valor.items():
        print(f"•Atributo: {atributo.ljust(18)} | Linha: {linha_atributo}")
        print(f"•Valor do Atributo: {valor}\n")
    print("")

style_tag = re.search(r'<style>(.*?)</style>', entrada_html, re.DOTALL)
if style_tag:
  css_content = style_tag.group(1)
  css_rules = re.findall(r'([a-zA-Z0-9\s,.#\-]+)\s*{([^}]*)}', css_content)
  print("----------------------------------------------------")
  print('\033[0m' + "Seletores Dentro da tag style" + '\033[0m')
  print("----------------------------------------------------")
  for selector, properties in css_rules:
    print("")
    print(f"Seletor: {selector.strip()}\n")
    properties = properties.strip()
    css_properties = re.findall(r'([a-zA-Z-]+)\s*:\s*([^;]+);', properties)
    for property_name, property_value in css_properties:
      print(f"  • Atributo: {property_name.strip()}")
      print(f"  • Valor do Atributo: {property_value.strip()}\n")