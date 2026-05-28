# para programar esse exemplo, será necessário 3 tabelas hash, grafo, custos, pais
# dentro do grafo(chave) possui vértices(valor), dentro do vértice(chave) possui vizinhos(valor), dentro dos vizinhos(chave) possui peso(chave)
# o vértice final n tem vizinhos
# é necessário criar um array com os processadoasa, pois o grafo n precisa ser conferido mais de uma vez
# se qualquer um dos custos for atualizado, atualize tbm o pai

# grafo, que contém outros vértices
grafo = {}
grafo['inicio'] = {}
grafo['inicio']['a'] = 6
grafo['inicio']['b'] = 2
grafo['a'] = {}
grafo['a']['fim'] = 1

grafo['b'] = {}
grafo['b']['a'] = 3
grafo['b']['fim'] = 5

grafo['fim'] = {}

# tabela de custos
# representação do infinito em python:
infinito = float('int')
custos = {}
custos['a'] = 6
custos['b'] = 2
custos['fim'] = infinito

# tabela de pais
pais = {}
pais['a'] = 'inicio'
pais['b'] = 'inicio'
pais['fim'] = None

# array de processados
processados = []

# função ache_no_custo_mais_baixo
def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float('inf')
    nodo_custo_mais_baixo = None
    for nodo in custos: # vá por cada vértice
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados: # se for o vértice menor do custo e até o momento e não tiver sido processado
            custo_mais_baixo = custo # atribua como o novo vértice de menor custo
            nodo_custo_mais_baixo = nodo
        return nodo_custo_mais_baixo

# algoritmo Dijkstra em python:
nodo = ache_no_custo_mais_baixo(custos) # encontra o custo mais baixo que n foi processado
while nodo is not None: # caso todos os vértices tenham sido processados, esse laço while será finalizado
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys(): # percore todos os vizinhos desse vértice
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo: # caso seja mais barato chegar a um vizinho a partir desse vértice...
            custos[n] = novo_custo # ...atualiza o custo dele
            pais[n] = nodo # esse vértice se torna o novo pai para o vizinho
    processados.append(nodo) # marca o vértice processado
    nodo = ache_no_custo_mais_baixo(custos) # encontra o próximo vértice a ser processado e o algoritmo é repetido



