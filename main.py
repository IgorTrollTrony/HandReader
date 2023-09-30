import re

entrada_html = """<html lang="pt-br">
<head>
    <title>Exemplo de HTML com Duas Divs</title>
</head>
<body>
    <div>
      <br>
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
tags_fechamento = []
nivel = 0
for tag, atributos in tags:
  if '/' not in tag:
    if not tag.endswith('/'):
      print(f"Tag de abertura: {tag}, Nível: {nivel}")
      if not tag.lower() in ['br', 'img', 'h']:
        tags_abertura.append(tag)
        nivel += 1
  else:
    tag_fechamento = tag[1:]
    if tags_abertura and tags_abertura[-1] == tag_fechamento:
      nivel -= 1
      tags_fechamento.append("Tag de fechamento : "+str(tag_fechamento) +" "+"Nivel : "+ str(nivel))
      tags_abertura.pop()
print("")
for tag in tags_fechamento:
  print(tag)

#Organizaçao da saida de resultados
