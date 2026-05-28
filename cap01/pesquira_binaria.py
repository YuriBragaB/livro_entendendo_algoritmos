def pesquisa_binaria(lista,item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = int((baixo + alto) / 2) # o livro esqueceu de botar o int()
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3)) # 1, o indice do 3 é 1
print(pesquisa_binaria(minha_lista, -1)) # nome
