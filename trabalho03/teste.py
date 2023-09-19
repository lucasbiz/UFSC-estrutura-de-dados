class Mar:

    def __init__(self):
        self.mar = []
        self.linhas = 0
        self.colunas = 0


    def ler_entrada(self):
        while True:
            linha = input()
            if not linha:
                break
            linha_aux = list(linha)
            linha_int = []
            for num in linha_aux:
                num = int(num)
                linha_int.append(num)

            self.mar.append(linha_int)
            self.colunas += 1
            self.linhas += 1

    def encontrar_maior_ilha(self):

        if not self.mar:
            return 0  # Matriz vazia

        maior_area = 0

        for l in range(self.linhas):
            for c in range(self.colunas):
                if self.mar[l][c] == 1:
                    area = self.calc_area(l, c)
                    if area > maior_area:  
                        maior_area = area

        return maior_area

    def calc_area(self, l, c):
        pilha = [(l, c)]  # Inicializa a pilha com a coordenada de partida
        area = 0

        while pilha:
            x, y = pilha.pop()

            if 0 <= x < self.linhas and 0 <= y < self.colunas and self.mar[x][y] == 1:
                self.mar[x][y] = -1  # Marque como visitado
                area += 1

                # Empilhe as coordenadas dos vizinhos
                pilha.append((x - 1, y))
                pilha.append((x + 1, y))
                pilha.append((x, y - 1))
                pilha.append((x, y + 1))

        return area





mar1 = Mar()
mar1.ler_entrada()
print(mar1.mar)
print('-----------------')
print(mar1.encontrar_maior_ilha())

