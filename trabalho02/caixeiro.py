import math

# problema do caixeiro viajante
# viagem de uma cidade i ate uma cidade j implica num custo Cij > 0

#recebe as coordenadas

#calcula o custo

# coord
#  0   1
# [Xi, Yi]


class Node:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def acresc_ponto(self, x, y):
        novo_no = Node(x, y)
        if not self.head: #None é considerado false, então not false = true, significando que a lista está vazia
            self.head = novo_no
        
        else:
            no_atual = self.head

            while no_atual.next: #verifica se o proximo item é None ou não, se for None o loop para, pois None == False
                no_atual = no_atual.next
            no_atual.next = novo_no

    def calcular_distancia_total(self):
        if not self.head:
            return 0  # Lista vazia

        distancia_total = 0
        no_atual = self.head

        while no_atual:

            if no_atual.next:
                prox_no = no_atual.next
            else:
                prox_no = self.head

            distancia = math.sqrt((int(no_atual.x) - int(prox_no.x))**2 + (int(no_atual.y) - int(prox_no.y))**2)
            distancia_total += distancia
            no_atual = no_atual.next

            if no_atual == self.head:
                break

        return distancia_total


    def troca_local(self):
        if not self.head or not self.head.next:
            return  # Lista vazia ou com apenas um ponto, não há o que trocar

        no_atual = self.head
        primeiro_no = self.head
        distancia_anterior = self.calcular_distancia_total()

        while no_atual:
            prox_no = no_atual.next

            if not prox_no:
                prox_no = self.head

            temp_x = no_atual.x
            temp_y = no_atual.y

            no_atual.x = prox_no.x
            no_atual.y = prox_no.y

            prox_no.x = temp_x
            prox_no.y = temp_y

            nova_distancia = self.calcular_distancia_total()

            if nova_distancia >= distancia_anterior:
                temp_x = no_atual.x
                temp_y = no_atual.y

                no_atual.x = prox_no.x
                no_atual.y = prox_no.y

                prox_no.x = temp_x
                prox_no.y = temp_y
            else:
                distancia_anterior = nova_distancia

            no_atual = no_atual.next

            if no_atual == primeiro_no:
                break
        nova_lista = self.tolist()
        return nova_lista

    def tolist(self):
        dados_no = [] #lista onde vao os dados
        no_atual = self.head #começa pela Kabeça

        #enquanto houver nos, coloca os dados deles na lista dados_no
        while no_atual:
            dados_no.append([no_atual.x, no_atual.y])
            no_atual = no_atual.next
        
        return dados_no #retorna a lista de dados




def pegar_pontos():
    coordenada = input()
    lista_coordenadas = []

    while coordenada != '-1 -1':
        coordenadas_separadas = coordenada.split()
        lista_coordenadas.append(coordenadas_separadas)
        coordenada = input()
    
    return lista_coordenadas


lista_encadeada = LinkedList()
lista_pontos = [
    [56, 71], [73, 29], [73, 38], [18, 47], [70, 85],
    [40, 50], [6, 54], [40, 56], [76, 82], [10, 30],
    [68, 81], [36, 73], [66, 13], [57, 13], [94, 38],
    [38, 85], [22, 9], [62, 97], [26, 67], [40, 5]
]

for ponto in lista_pontos:
    lista_encadeada.acresc_ponto(ponto[0], ponto[1])

print(round(lista_encadeada.calcular_distancia_total(), 2))

# Realizar a troca local até que não haja melhora
distancia_anterior = lista_encadeada.calcular_distancia_total()
nova_distancia = distancia_anterior

while distancia_anterior >= nova_distancia:
    lista_encadeada.troca_local()
    distancia_anterior = nova_distancia
    nova_distancia = lista_encadeada.calcular_distancia_total()
    print(nova_distancia)
    
    if nova_distancia == distancia_anterior:
        break
    
print(round(nova_distancia, 2))



