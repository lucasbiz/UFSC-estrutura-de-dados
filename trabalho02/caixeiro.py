# problema do caixeiro viajante
# viagem de uma cidade i ate uma cidade j implica num custo Cij > 0

#recebe as coordenadas
coordenada = input()
lista_coordenadas = []

while coordenada != '-1 -1':
    coordenadas_separadas = coordenada.split()
    lista_coordenadas.append(coordenadas_separadas)
    coordenada = input()


#calcula o custo

# coord
#  0   1
# [Xi, Yi]

def calculo_custo(lista_coordenadas, ind_analisado, proxima_coord):
    custo = (((int(lista_coordenadas[ind_analisado][0]) - int(lista_coordenadas[proxima_coord][0]))**2) + ((int(lista_coordenadas[ind_analisado][1]) - int(lista_coordenadas[proxima_coord][1]))**2))**(1/2)

    return custo


ind_analisado = 0
proxima_coord = ind_analisado + 1
custo_viagem = 0
tam = len(lista_coordenadas)

while ind_analisado < tam:
    custo = calculo_custo(lista_coordenadas, ind_analisado, proxima_coord)

    custo_viagem += custo
    ind_analisado += 1

custo_voltar_inicio = calculo_custo(lista_coordenadas, tam-1, 0)

custo_viagem += custo_voltar_inicio

print(round(custo_viagem,2))
