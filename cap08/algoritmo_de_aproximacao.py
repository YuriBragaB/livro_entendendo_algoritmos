estados_abranger = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az',]) # cria um conjunto(set) decorrente de um array, conjuntos n podem ter elementos duplicados, lista dos estados que deseja abranger

estacoes = {} # tabela hass com as estações
estacoes['kum'] = set(['id', 'nv', 'ut'])
estacoes['kdois'] = set(['wa', 'id', 'mt'])
estacoes['ktres'] = set(['or', 'nv', 'ca'])
estacoes['kquatro'] = set(['nv', 'ut'])
estacoes['kcinco'] = set(['ca', 'az'])

estacoes_final = set() # armazena o conjunto final de estações
while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()
    for estacao, estados_por_estacao in estacoes.items():
        cobertos = estados_abranger & estados_por_estacao # interseção, elemento que é comum nos dois conjuntos
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos
    estados_abranger -= estados_cobertos
    estacoes_final.add(melhor_estacao) 

print(estacoes_final)
