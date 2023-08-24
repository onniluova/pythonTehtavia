kaupunki = ""
lista = []
laskuri = int(5)

while (laskuri > 0):
    kaupunki = input(("Syötä kaupungin nimi: "))
    lista.append(kaupunki)
    laskuri -= 1

for i in lista:
    print(i + "\n")
