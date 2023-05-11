b = [1, 4, 4, 4, 5, 3]


def migratoryBirds(b:list):
    lista = {}
    for tipo in set(b):
        lista[tipo] = b.count(tipo)
    candidates_birds = [k for k,v in lista.items() if v == max(lista.values())]
    return min(candidates_birds)

a = migratoryBirds(b)
print(a)