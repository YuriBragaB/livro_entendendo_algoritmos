def buscar_menor (arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenar_por_selecao(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = buscar_menor(arr)
        novo_arr.append(arr.pop(menor))

    return novo_arr

print(ordenar_por_selecao([2,6,2,1,6,4,9]))