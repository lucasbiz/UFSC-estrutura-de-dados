
class Tabuleiro:

    def __init__(self):
        self.tabuleiro = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
    
    def pegar_posicoes(self):
        n = 0
        posicoes = []
        while n < 2:
            posicao = input()
            x = self.letra_para_numero(posicao[0]) - 1
            y = int(posicao[1]) - 1
            posicoes.append((x, y))
            n += 1

        return posicoes

    def coord_valida(self, x, y):
        if x >= 0 and x <= 7 and y >= 0 and y <= 7:
            return True
        else:
            return False
    
    def letra_para_numero(self, letra):

        posicoes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        converter = letra
        i = 0
        for el in posicoes:
            if el == converter:
                converter = i + 1
            i += 1
        return (converter)  

    def movimentos_minimos_para_destino(self, inicial, destino):
        # Todos os movimentos possível que o cavalo pode fazer (em forma de índices)
        dx = [-2, -2, -1, -1, 1, 1, 2, 2]
        dy = [-1, 1, -2, 2, -2, 2, -1, 1]

        fila = [(inicial[0], inicial[1], 0)]  # Usando uma lista como fila.
        visitado = self.tabuleiro  # Tabuleiro 8x8

        while fila:
            x, y, movimentos = fila.pop(0)  # Remove o primeiro elemento da fila.

            if (x, y) == destino:
                return movimentos

            for i in range(8):
                novo_x = x + dx[i]
                novo_y = y + dy[i]

                if self.coord_valida(novo_x, novo_y): 
                    if visitado[novo_x][novo_y] == 0:
                        visitado[novo_x][novo_y] = 1
                        fila.append((novo_x, novo_y, movimentos + 1))



caminho_cavalo = Tabuleiro()

coordenadas = caminho_cavalo.pegar_posicoes()

resultado = caminho_cavalo.movimentos_minimos_para_destino(coordenadas[0], coordenadas[1])
print(f"Movimentos: {resultado}")

