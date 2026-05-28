# dividir para conquistar

def soma(lista):
    # if lista == []:
    #     return 0
    # return lista[0] + soma(lista[1:])
    return 0 if lista == [] else lista[0] + soma(lista[1:])

print(soma([1,2 ,3 ,4 ,5]))

def contar(lista):
    return 0 if lista == [] else 1 + contar(lista[1:])

print(contar([1, 3, 5, 8]))


def maior(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maior(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max
    
print(maior([4,5,2,9,7,6]))