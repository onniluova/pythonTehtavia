def palautaParilliset(self):
    lista = []
    for l in range(len(self)):
        if (l % 2 == 0):
            lista.append(l)
    return print("Parilliset: " + str(lista))