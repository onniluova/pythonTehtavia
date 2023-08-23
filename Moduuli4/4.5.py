laskuri = int(0)

tunnus = ("tunnus")
salasana = ("salasana")

syote1 = ""
syote2 = ""

while syote1 != tunnus and syote2 != salasana and laskuri < 5:
    syote1 = (input("Syötä tunnus: "))
    syote2 = (input("Syötä salasana: "))
    laskuri +=1

if syote1 == tunnus and syote2 == salasana:
    print("Tervetuloa")

if laskuri == 5:
    print("Pääsy evätty")