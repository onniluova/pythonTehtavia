kertoja = int(100)
lentoasemat = {}

valintaindex = 0

print("Haluatko syöttää uuden lentoaseman (1), hakea lentoaseman tiedot (2) vai lopettaa? (3)")
valinta = int(input("Valitse 1, 2 tai 3: "))
index = valinta

while index != 3:
    valinta = int(input("Valitse 1, 2 tai 3: "))
    index = valinta
    if valinta == 1:
        icao = (input("Uusi ICAO koodi: "))
        lentoasema = (input("Uuden lentokentän nimi: "))
        lentoasemat[icao] = lentoasema


    elif valinta == 2:
        valinta3 = str(input("Syötä ICAO koodi: "))
        if valinta3 in lentoasemat.keys():
            print(lentoasemat[icao])
        else:
            print("ICAO koodia löytynyt.")

    elif valinta == 3:
        print("Loppu")
        exit()
