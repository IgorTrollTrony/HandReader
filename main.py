class TreeNode:
  def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None

class BinaryTree:
  def __init__(self):
      self.root = None

  def inserir(self, chave):
      self.root = self._inserir(self.root, chave)

  def _inserir(self, raiz, chave):
      if raiz is None:
          return TreeNode(chave)
      if chave < raiz.key:
          raiz.left = self._inserir(raiz.left, chave)
      elif chave > raiz.key:
          raiz.right = self._inserir(raiz.right, chave)
      return raiz

  def adicionar_no(self, chave_pai, chave_novo_no, posicao):
      pai = self._buscar(self.root, chave_pai)
      if pai:
          if posicao == 'esquerda' and pai.left is None:
              pai.left = TreeNode(chave_novo_no)
          elif posicao == 'direita' and pai.right is None:
              pai.right = TreeNode(chave_novo_no)
          else:
              print(f"Erro: posição inválida ou nó já existe em {posicao} para o pai {chave_pai}")
      else:
          print(f"Erro: Pai {chave_pai} não encontrado")

  def excluir(self, chave):
      self.root = self._excluir(self.root, chave)

  def _excluir(self, raiz, chave):
      if raiz is None:
          return raiz
      if chave < raiz.key:
          raiz.left = self._excluir(raiz.left, chave)
      elif chave > raiz.key:
          raiz.right = self._excluir(raiz.right, chave)
      else:
          # Caso 1: Nó com no máximo um filho
          if raiz.left is None:
              return raiz.right
          elif raiz.right is None:
              return raiz.left

          # Caso 2: Nó com dois filhos, encontrar o sucessor in-order
          raiz.key = self._min_value_node(raiz.right).key
          raiz.right = self._excluir(raiz.right, raiz.key)

      return raiz

  def buscar(self, chave):
      return self._buscar(self.root, chave)

  def _buscar(self, raiz, chave):
      if raiz is None or raiz.key == chave:
          return raiz
      if chave < raiz.key:
          return self._buscar(raiz.left, chave)
      return self._buscar(raiz.right, chave)

  def _min_value_node(self, no):
      atual = no
      while atual.left is not None:
          atual = atual.left
      return atual

  def travessia_em_ordem(self):
      resultado = []
      self._travessia_em_ordem(self.root, resultado)
      return resultado

  def _travessia_em_ordem(self, raiz, resultado):
      if raiz:
          self._travessia_em_ordem(raiz.left, resultado)
          resultado.append(raiz.key)
          self._travessia_em_ordem(raiz.right, resultado)

  def travessia_pre_ordem(self):
      resultado = []
      self._travessia_pre_ordem(self.root, resultado)
      return resultado

  def _travessia_pre_ordem(self, raiz, resultado):
      if raiz:
          resultado.append(raiz.key)
          self._travessia_pre_ordem(raiz.left, resultado)
          self._travessia_pre_ordem(raiz.right, resultado)

  def travessia_pos_ordem(self):
      resultado = []
      self._travessia_pos_ordem(self.root, resultado)
      return resultado

  def _travessia_pos_ordem(self, raiz, resultado):
      if raiz:
          self._travessia_pos_ordem(raiz.left, resultado)
          self._travessia_pos_ordem(raiz.right, resultado)
          resultado.append(raiz.key)

  def altura_arvore(self):
      return self._altura_arvore(self.root)

  def _altura_arvore(self, raiz):
      if raiz is None:
          return 0
      altura_esquerda = self._altura_arvore(raiz.left)
      altura_direita = self._altura_arvore(raiz.right)
      return max(altura_esquerda, altura_direita) + 1

  def profundidade_no(self, chave):
      return self._profundidade_no(self.root, chave, 0)

  def _profundidade_no(self, raiz, chave, profundidade):
      if raiz is None:
          return -1
      if raiz.key == chave:
          return profundidade
      profundidade_esquerda = self._profundidade_no(raiz.left, chave, profundidade + 1)
      profundidade_direita = self._profundidade_no(raiz.right, chave, profundidade + 1)
      if profundidade_esquerda != -1:
          return profundidade_esquerda
      return profundidade_direita

  def contar_nos(self):
      return self._contar_nos(self.root)

  def _contar_nos(self, raiz):
      if raiz is None:
          return 0
      return 1 + self._contar_nos(raiz.left) + self._contar_nos(raiz.right)

# Exemplo de uso:
arvore = BinaryTree()
arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)

print("Travessia em Ordem:", arvore.travessia_em_ordem())
print("Travessia Pré-Ordem:", arvore.travessia_pre_ordem())
print("Travessia Pós-Ordem:", arvore.travessia_pos_ordem())

no_a_excluir = 30
print(f"Excluindo nó com chave {no_a_excluir}")
arvore.excluir(no_a_excluir)
print("Travessia em Ordem após exclusão:", arvore.travessia_em_ordem())

chave_a_buscar = 60
print(f"Buscando nó com chave {chave_a_buscar}: {arvore.buscar(chave_a_buscar) is not None}")

print("Altura da Árvore:", arvore.altura_arvore())

chave_profundidade = 40
print(f"Profundidade do nó com chave {chave_profundidade}: {arvore.profundidade_no(chave_profundidade)}")

print("Número de nós na árvore:", arvore.contar_nos())
# Adicionando um novo nó à esquerda do nó com a chave 60
arvore.adicionar_no(60, 55, 'esquerda')

# Exibindo a travessia em ordem após adição do novo nó
print("Travessia em Ordem após adição de novo nó:", arvore.travessia_em_ordem())
