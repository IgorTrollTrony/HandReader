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
</html>"""

#/? pode ou ter /
#\w+ um ou mais caracteres de palavra
tags = re.findall(r'<(/?\w+)([^>]*)>', entrada_html)

tags_abertura = []
tags_fechamento = []
nivel = 0
linhas = entrada_html.splitlines()
atributos = {}  # Dicionário para armazenar os atributos

for linha, linha_html in enumerate(linhas, start=1):
    for tag, atributos_str in re.findall(r'<(/?\w+)([^>]*)>', linha_html):
        if '/' not in tag:
            if not tag.endswith('/'):
                print(f"Tag de abertura   : {tag.ljust(9)} | Nível: {nivel} | Linha: {linha}")
                if not tag.lower() in ['br', 'img', 'h']:
                    tags_abertura.append(tag)
                    nivel += 1  
        else:
            tag_fechamento = tag[1:]
            if tags_abertura and tags_abertura[-1] == tag_fechamento:
                nivel -= 1
                tags_fechamento.append("Tag de fechamento : " + str(tag_fechamento.ljust(9)) + " " + "| Nível : " + str(
                    nivel) + "| Linha: " + str(linha))
                tags_abertura.pop()
        atributos_str = atributos_str.strip()
        if atributos_str:
            atributos_str = re.findall(r'(\w+)="([^"]*)"', atributos_str)
            for atributo, valor in atributos_str:
                atributos[tag] = atributos.get(tag, {})
                atributos[tag][atributo] = valor


print("----------------------------------------------------")
for tag in tags_fechamento:
    print(tag)
for tag, atributo_valor in atributos.items():
    print("----------------------------------------------------")
    print(f"Tag: {tag}\n")
    for atributo, valor in atributo_valor.items():
        print(f"  • Atributo: {atributo}")
        print(f"  • Valor do Atributo: {valor}\n")

  #identificaçao de atributos de tags
  