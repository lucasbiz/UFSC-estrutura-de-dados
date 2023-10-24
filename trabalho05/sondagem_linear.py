class Vetor:

    def __init__(self):
        self.itens = []

    def construir_vetor(self, parametros):
        tamanho_vetor = int(parametros[0])

        for i in range(0, tamanho_vetor):
            self.itens.append(-1)

        parametros.pop(0)

        for item in parametros:
            
            if item == '0' or item == '1':
                operacao = item
            
            else:
                if operacao == '0':
                    posicao_insercao = len(item) % tamanho_vetor
                    self.adicionar_item(item, posicao_insercao)

                elif operacao == '1':
                    posicao_remocao = len(item) % tamanho_vetor
                    self.remover_item(item, posicao_remocao)




    def adicionar_item(self, item, posicao_insercao):
        
        tamanho_vetor = len(self.itens) - 1
        contador = 0
        adicionado = False

        while adicionado == False:

            if self.itens[posicao_insercao] == -1 or self.itens[posicao_insercao] == -2:
                self.itens[posicao_insercao] = item
                adicionado = True
            else:
                if posicao_insercao == tamanho_vetor:
                    posicao_insercao = 0
                else:
                    posicao_insercao += 1

            if contador == tamanho_vetor:
                break
            contador += 1

        # se nao tiver lugar, fazer a sondagem linear pelo local vago mais proximo

    def remover_item(self, item, posicao_remocao):

        tamanho_vetor = len(self.itens) - 1
        contador = 0
        removido = False

        while removido == False:

            if self.itens[posicao_remocao] == item:
                self.itens[posicao_remocao] = -2
                removido = True
            else:
                if posicao_remocao == tamanho_vetor:
                    posicao_remocao = 0
                else:
                    posicao_remocao += 1

            if contador == tamanho_vetor:
                break
            contador += 1

    def mostra_vetor(self):

        for item in self.itens:
            print(item)






vetor = Vetor()

item_vetor = input()
entradas = []

while item_vetor != '-1':
    entradas.append(item_vetor)
    item_vetor = input()

vetor.construir_vetor(entradas)

vetor.mostra_vetor()