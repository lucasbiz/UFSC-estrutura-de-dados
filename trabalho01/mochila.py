# input_item = input()
lista_itens = [['18', '5', '1'],['12', '4', '2'],['15', '5', '3'],['10', '2', '2'],['15', '6', '5'],['4', '2', '5']]

indice = 0
for item in lista_itens:
    item.append(indice)
    indice += 1

# Ui Wi Di
# Utilidade, peso e quantidade
# Ui/Wi

# indice = 0
# while input_item != '-1 -1 -1':
#     item = input_item.split()
#     item.append(indice)
#     lista_itens.append(item)
#     indice += 1
#     input_item = input()

capacidade_mochila = input()

#insertion sort

posicao = 1

while posicao < len(lista_itens):

    pos_analisada = posicao
    contador_int = pos_analisada - 1

    while contador_int >= 0:

        num_analisado = int(lista_itens[pos_analisada][0])/int(lista_itens[pos_analisada][1])
        lista_analisada = lista_itens[pos_analisada]

        if num_analisado > int(lista_itens[contador_int][0])/int(lista_itens[contador_int][1]):
            lista_itens[pos_analisada] = lista_itens[contador_int]
            lista_itens[contador_int] = lista_analisada
            pos_analisada -= 1

        contador_int -= 1
    posicao += 1


peso_da_mochila = 0

for item in lista_itens:

    peso_item = int(item[1])
    quantidade_item = int(item[2])

    total = peso_item*quantidade_item
    peso_da_mochila += total

    while peso_da_mochila > capacidade_mochila and quantidade_item > 0:
        peso_da_mochila -= total
        quantidade_item -= 1
        total = peso_item*quantidade_item
        peso_da_mochila += total

    if quantidade_item > 0:
        print(f'{item[3]} {quantidade_item}')
    



