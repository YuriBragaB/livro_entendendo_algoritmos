# Valores mercado

caderno = dict()

caderno['maçã'] = 0.67 # uma maçã custa 1.49
caderno ['leite'] = 1.49 # o leite custa 1.49
caderno['abacate'] = 1.49

print(caderno)

print(caderno['abacate']) # o preço de um abacate

# Lista telefónica
lista_telefonica = {} # msm coisa de lista telefónica = dict()

lista_telefonica['jenny'] = 8675309
lista_telefonica['emergency'] = 911

print(lista_telefonica['jenny']) # número de telefone da jenny

# Evitando duas chaves iguais em uma tabela hash
votaram = {}
valor = votaram.get('tom') # a funçãon get(pegar), retornará um valor se 'Tom' já estiver na tabela hash.Caso contrário, ela retornará None(nada).Você pode usar essa funcionalidade para garantir se as pessoas já votaram

def verifica_eleitor(nome):
    if votaram.get(nome):
        print('Mande embora!')
    else:
        votaram[nome] = True
        print('Deixe votar!')

verifica_eleitor('tom')
# Deixe votar!
verifica_eleitor('mike')
# Deixe votar!
verifica_eleitor('mike')
# Mande embora!

# verificaçao de url

cache = {}

def pega_pagina(url):
    if cache.get(url): # se possuir dados
        return cache[url] # retorna os dados do cache
    else: # se nao possuir (None)
        dados = 'pega_dados_do_servidor(url)' # pede os dados
        cache[url] = dados # salva dados primeiro no seu cache
        return dados