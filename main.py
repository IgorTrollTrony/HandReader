import re

entrada_html = """<html> <head> <title> Compiladores </title> </head><body> <p style="color:red;background:blue;" id="abc"> Unipinhal </p> <br> </body></html>"""

#/? pode ou ter /
#\w+ um ou mais caracteres de palavra
tags = re.findall(r'<(/?\w+)([^>]*)>', entrada_html)
nivel = 0
for tag, atributos in tags:
  if '/' not in tag:
    print(f"Tag de abertura: {tag},Nivel : {nivel}")
    nivel += 1
  else:
    print(f"Tag de fechamento: {tag}")