# class Node:
#     def __init__(self, valor):
#         self.valor = valor
#         self.esquerda = None
#         self.direita = None

# class Arvore:

#     def __init__(self):
#         self.raiz = None
        
#     def construir_arvore(self, expressao):
#         prioridade = {'*': 2, '/': 2, '+': 1, '-': 1}
#         fila_saida = []
#         pilha_operadores = []

#         for token in expressao:
#             if token.isalpha():
#                 fila_saida.append(Node(token))

#             elif token in prioridade:
#                 while pilha_operadores and pilha_operadores[-1] in prioridade and prioridade[pilha_operadores[-1]] >= prioridade[token]:
#                     fila_saida.append(Node(pilha_operadores.pop()))
#                 pilha_operadores.append(token)

#         while pilha_operadores:
#             fila_saida.append(Node(pilha_operadores.pop()))
#             pilha = []

#         for node in fila_saida:
#             if node.valor in prioridade:
#                 node.direita = pilha.pop()
#                 node.esquerda = pilha.pop()
#             pilha.append(node)
#         return pilha[0]

#     def pre_ordem(self, node):
#         if node is None:
#             return ''
#         esquerda = pre_ordem(node.esquerda)
#         direita = pre_ordem(node.direita)

#         return node.valor + esquerda + direita

#     def pos_ordem(self, node):
#         if node is None:
#             return ''
#         esquerda = pos_ordem(node.esquerda)
#         direita = pos_ordem(node.direita)
#         return esquerda + direita + node.valor


# expressao = 'A*B+C*D-E'
# arvore = Arvore()
# raiz = arvore.construir_arvore(expressao)
# pre_ordem = arvore.pre_ordem(raiz)
# pos_ordem = arvore.pos_ordem(raiz)
# print('Notação Prefixada:', pre_ordem)
# print('Notação Posfixada:', pos_ordem)


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore:

    def __init__(self):
        self.raiz = None
        
    def construir_arvore(self, expressao):
        prioridade = {'*': 2, '/': 2, '+': 1, '-': 1}
        fila_saida = []
        pilha_operadores = []

        for token in expressao:
            if token.isalpha():
                fila_saida.append(Node(token))

            elif token in prioridade:
                while pilha_operadores and pilha_operadores[-1] in prioridade and prioridade[pilha_operadores[-1]] >= prioridade[token]:
                    fila_saida.append(Node(pilha_operadores.pop()))
                pilha_operadores.append(token)

        while pilha_operadores:
            fila_saida.append(Node(pilha_operadores.pop()))

        pilha = []
        for node in fila_saida:
            if node.valor in prioridade:
                node.direita = pilha.pop()
                node.esquerda = pilha.pop()
            pilha.append(node)
        return pilha[0]

    def pre_ordem(self, node):
        if node is None:
            return ''
        esquerda = self.pre_ordem(node.esquerda)
        direita = self.pre_ordem(node.direita)

        return node.valor + esquerda + direita

    def pos_ordem(self, node):
        if node is None:
            return ''
        esquerda = self.pos_ordem(node.esquerda)
        direita = self.pos_ordem(node.direita)
        return esquerda + direita + node.valor


expressao = 'A*B+C*D-E'
arvore = Arvore()
raiz = arvore.construir_arvore(expressao)
pre_ordem = arvore.pre_ordem(raiz)
pos_ordem = arvore.pos_ordem(raiz)
print(pre_ordem)
print(pos_ordem)