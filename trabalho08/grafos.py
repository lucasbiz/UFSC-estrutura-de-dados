from collections import deque

class Grafo:
    def __init__(self, num_vertices):
        # Inicializa o grafo e a lista de graus de entrada
        self._grafo = {}
        self._indegree = []
        for i in range(num_vertices):
            self._grafo[i] = []
            self._indegree.append(0)

    def adicionar_aresta(self, origem, destino):
        # Adiciona uma aresta ao grafo e atualiza o grau de entrada do vértice de destino
        self._grafo[origem].append(destino)
        self._indegree[destino] += 1

    def ordenacao(self):
        # Cria uma fila para armazenar os vértices com grau de entrada 0
        q = deque()
        for i in range(len(self._indegree)):
            if self._indegree[i] == 0:
                q.append(i)

        # Inicializa a lista de semestres
        semestres = [0] * len(self._indegree)

        # Processa os vértices na fila
        while q:
            vertice = q.popleft()
            for vizinho in self._grafo[vertice]:
                self._indegree[vizinho] -= 1
                if self._indegree[vizinho] == 0:
                    q.append(vizinho)
                    semestres[vizinho] = semestres[vertice] + 1

        # Retorna o número máximo de semestres
        return max(semestres) + 1


entrada = input()
entradas = []

while entrada != '-1,-1':
    entradas.append(entrada)
    entrada = input()

num_disciplinas = int(entradas[0])
max_disciplina = max(int(arco.split(",")[1]) for arco in entradas[1:])

g = Grafo(max(max_disciplina, num_disciplinas) + 1)

for arco in entradas[1:]:
    i, j = map(int, arco.split(","))
    g.adicionar_aresta(i, j)

print(g.ordenacao())