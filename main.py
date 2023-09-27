import re

entrada_html = """<html lang="pt-br">
<head>
    <title>Exemplo de HTML com Duas Divs</title>
</head>
<body>
    <div>
        <h1>Div 1</h1>
        <p><span></span></p>
    </div>
    <div>
        <h1>Div 2</h1>
        <p>Esta é a segunda div.</p>
    </div>
</body>
</html>"""

#/? pode ou ter /
#\w+ um ou mais caracteres de palavra
tags = re.findall(r'<(/?\w+)([^>]*)>', entrada_html)

tags_abertura = []
nivel = 0
for tag, atributos in tags:
  if '/' not in tag:
    print(f"Tag de abertura: {tag}, Nível: {nivel}")
    tags_abertura.append(tag)
    nivel += 1  # Aumenta o nível
  else:
     tag_fechamento = tag[1:]  
     if tags_abertura and tags_abertura[-1] == tag_fechamento:
        nivel -= 1
        print(f"Tag de fechamento: {tag_fechamento}, Nível: {nivel}")
        tags_abertura.pop()  
