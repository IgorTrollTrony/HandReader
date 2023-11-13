import re

entrada_html = """<html>
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
encoding_match = re.search(r'<meta\s+charset=["\']?([^"\']+)["\']?\s*/?>',
                           entrada_html)
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
        if not tag.lower() in ['br', 'img', 'h','input','meta']:
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
print('\033[1m' + "Contudo de tags de texto" + '\033[0m')
print("----------------------------------------------------")
# Lista de tags que podem ter texto dentro
tags_com_texto = [
    "p", "h1", "h2", "h3", "h4", "span", "a", "strong", "b", "em", "i", "u",
    "s", "del", "ins", "mark", "abbr", "cite", "code", "pre"
]

# Divida o HTML em linhas
linhas = entrada_html.splitlines()
for linha_numero, linha in enumerate(linhas, start=1):
  for tag in tags_com_texto:
    regex = f'<{tag}[^>]*>(.*?)</{tag}>'
    tags_encontradas = re.findall(regex, linha, re.DOTALL)
    for conteudo in tags_encontradas:
      print(f"Tag: {tag.ljust(15)} | Linha:{str(linha_numero)}\n")
      print(f"Conteúdo: {conteudo.strip()}\n\n")
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

E