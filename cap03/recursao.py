# exemplo utiliza pseudocódigo
# o que esta entre aspas é o que está dando erro no código

# achar uma chave, que está dentro de uma caixa, pode possuir uma caixa dentro de outra caixa
def procure_pela_chave (caixa_principal):
    pilha ='main_box'.crie_uma_pilha_para_buscar()
    while pilha is not 'vazia':
        caixa = pilha.pegue_caixa()
        for item in caixa:
            if item.e_uma_caixa():
                pilha.append(item)
            elif item.e_uma_chave():
                print ('achei a chave!')


# exemplo com recursão
def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item) # recursao, a funcao se chamando novamente
        elif item.e_uma_chave():
            print('achei a chave')


# chamada recursiva + pilha de chamadas
def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x - 1) # é como se o x fosse se acumulando, fica guardado no espaço da memória até a pilha de chamadas acabar, quando acaba todos os valores são multiplicados
    

print(fat(5))