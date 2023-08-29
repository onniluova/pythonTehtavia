kuukaudet = ("tammi", "helmi", "maalis", "huhti", "touko", "kesä", "heinä", "elo", "syys", "loka", "marras", "joulu")
vuodenajat = ("kevät", "kesä", "syksy", "talvi")

numero = int(input("Syötä kuukauden numero: "))

if numero <= 3:
    print(vuodenajat[0])

elif numero >= 3 and numero <= 6:
    print(vuodenajat[1])

elif numero >= 6 and numero <= 9:
    print(vuodenajat[2])

elif numero >= 9 and numero <= 12:
    print(vuodenajat[3])