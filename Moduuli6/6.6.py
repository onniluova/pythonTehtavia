class pizza:
    def __init__(self, hinta, halkaisija):
        self.hinta = hinta
        self.halkaisija = halkaisija

def pizzanNelioHinta (self):
    neliometri = float(self.halkaisija % 10000)
    hinta = float(self.hinta / neliometri)
    return hinta

#Alla olevat olisi hyvä olla erillisessä tiedostossa selkeyden vuoksi
pizza1hinta = int(input("Syötä pizza 1 hinta: "))
pizza1halkaisija = int(input("Syötä pizza 1 halkaisija: "))

pizza2hinta = int(input("Syötä pizza 2 hinta: "))
pizza2halkaisija = int(input("Syötä pizza 2 halkaisija: "))

p1 = pizza(pizza1hinta, pizza1halkaisija)
p2 = pizza(pizza2hinta, pizza2halkaisija)

if pizzanNelioHinta(p1) < pizzanNelioHinta(p2):
    print("Pizzan 1 hinta: " + str(pizzanNelioHinta(p1)) + " euroa per neliömetri ja parempi hintalaatusuhteeltaan.")

elif pizzanNelioHinta(p1) == pizzanNelioHinta(p2):
    print("Pizzat ovat samanhintaiset!")

else:
    print("Pizzan 2 hinta: " + str(pizzanNelioHinta(p2)) + " euroa per neliömetri ja parempi hintalaatusuhteeltaan.")