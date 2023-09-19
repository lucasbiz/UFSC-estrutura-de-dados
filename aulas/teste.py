import math

def distancia_euclidiana(p1, p2):
    # Calcula a distância euclidiana entre dois pontos p1 e p2
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calcular_distancia_total(lista_pontos):
    distancia_total = 0
    n = len(lista_pontos)

    for i in range(n - 1):
        # Calcula a distância entre o ponto atual e o próximo ponto
        distancia = distancia_euclidiana(lista_pontos[i], lista_pontos[i + 1])
        distancia_total += distancia

    # Calcula a distância entre o último ponto e o ponto inicial
    distancia_final = distancia_euclidiana(lista_pontos[-1], lista_pontos[0])
    distancia_total += distancia_final

    return distancia_total

# Exemplo de uso com uma lista de pontos
lista_pontos = [[0, 0], [10, 0], [20, 10], [20, 0], [10, 10]]
distancia_total = calcular_distancia_total(lista_pontos)

print(f"A distância total percorrida é: {distancia_total:.2f}")
