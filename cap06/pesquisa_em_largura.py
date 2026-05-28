# código final para pesquisa em largura:
from collections import deque

grafo = {}
grafo['voce'] = ['alice','bob','claire'] # voce = vertice, atribuição = arestas
grafo['bob'] = ['anuj', 'peggy']
grafo['alice'] = ['peggy']
grafo['claire'] = ['thom', 'jonny']
grafo['anuj'] = []
grafo['peggy'] = []
grafo['thom'] = []
grafo['jonny'] = []

def pessoa_e_vendedor(nome):
    return nome == 'anuj'

def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = [] # esse vetor é a forma pela qual você mantém o registro das pessoas que já foram verificadas
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas: #  verifica essa pessoa somente se ela já não estiver verificada
            if pessoa_e_vendedor(pessoa):
                print(pessoa + ' é um vendedor de mangas')
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa) # marca essa pessoa como verificada
    return False

pesquisa('voce')