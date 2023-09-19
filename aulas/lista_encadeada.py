# Listas encadeadas, cada elemento possui uma referencia para o proximo, com o elemento final sendo None


class Node: # "nó"

    def __init__(self, data): # construtor do nó
        self.data = data # dado da lista
        self.next = None # Ponteiro para o próximo elemento, primeiramente vazio


class LinkedList:

    def __init__(self):
        self.head = None # onde a lista começa

    def insere_dados(self, dado):

        #cria um novo no com dado e ponteiro vazio para o prox no
        novo_no = Node(dado) 

        #se o primeiro item da lista for vazio, adiciona o novo nó a ele
        if self.head == None: 
            self.head = novo_no
            return

        # percorre a lista encadeada para encontrar o ultimo elemento
        no_atual = self.head
        while no_atual.next: 
            no_atual = no_atual.next
        
        #ultimo elemento vira o novo nó
        no_atual.next = novo_no 
        return

    # descobrir o tamanho da lista
    def length(self):

        # se a head for vazia, retorna 0
        if self.head == None:
            return 0

        #começa pela cabeça
        no_atual = self.head
        total = 0 #conta o tamanho da lista
        while no_atual: 
            total += 1
            no_atual = no_atual.next #passa por cada elemento da lista
        return total #retorna a quantidade de itens

    # conversão de lista encadeada para uma lista python normal
    def tolist(self):
        dados_no = [] #lista onde vao os dados
        no_atual = self.head #começa pela Kabeça

        #enquanto houver nos, coloca os dados deles na lista dados_no
        while no_atual:
            dados_no.append(no_atual.data)
            no_atual = no_atual.next
        
        return dados_no #retorna a lista de dados


    def display(self):
        conteudo = self.head

        if conteudo == None:
            print('-----------')
            print('Lista vazia')
            print('-----------')

        while conteudo:
            print(conteudo.data)
            conteudo = conteudo.next
        print('-------------')

    #reverter a lista encadeada, processo inverso
    def reverse_linkedlist(self):

        no_anterior = None
        no_atual = self.head

        while no_atual != None:
            next = no_atual.next
            no_atual.next = no_anterior
            no_anterior = no_atual
            no_atual = next
        self.head = no_anterior

lista1 = LinkedList()
lista1.display()

lista1.insere_dados(3)
lista1.insere_dados(7)
lista1.insere_dados(9)
lista1.insere_dados(12)

lista1.display()

print(lista1.tolist())
print(lista1.length())

lista1.reverse_linkedlist()
lista1.display()
