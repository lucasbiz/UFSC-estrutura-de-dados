lista_inicial = [3, 5, 9, 4, 8, 1]

posicao = 1

while posicao < len(lista_inicial):

    pos_analisada = posicao
    contador_int = pos_analisada - 1

    while contador_int >= 0:
        num_analisado = lista_inicial[pos_analisada]

        if num_analisado < lista_inicial[contador_int]:
            lista_inicial[pos_analisada] = lista_inicial[contador_int]
            lista_inicial[contador_int] = num_analisado
            pos_analisada -= 1

        contador_int -= 1
    posicao += 1
    

print(lista_inicial)
