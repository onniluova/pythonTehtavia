nimet = []
kysynimi = ("o")
index = kysynimi

while index != "":
    kysynimi = input("Syötä nimi: ")
    index = kysynimi
    if kysynimi in nimet:
        print("Aiemmin syötetty nimi: " + kysynimi)
    elif kysynimi != "":
        nimet.append(kysynimi)
        print("Uusi nimi: " + kysynimi)
print(str(nimet))