class Hissi:
    def __init__(self, akerros, ykerros, nkerros=0):
        self.akerros = int(akerros)
        self.ykerros = ykerros
        self.nkerros = akerros

    def siirryKerrokseen(self, kerrokset):
        if kerrokset < 0:
            while self.nkerros != kerrokset:
                self.kerrosAlas()
        elif kerrokset > 0:
            while self.nkerros != kerrokset:
                self.kerrosYlös()
        return print(self.nkerros)
    def kerrosYlös(self):
        self.nkerros += 1
    def kerrosAlas(self):
        self.nkerros -= 1

class talo:
    def __init__(self, akerros, ykerros, hissienlkm):
        self.akerros = akerros
        self.ykerros = ykerros
        self.hissienlkm = hissienlkm
        self.hissit = []

    def luoHissit(self):
        for _ in range(self.hissienlkm):
            hissi = Hissi(self.akerros, self.ykerros)
            self.hissit.append(hissi)
    def ajaHissiä(self, nro, kohdekerros):
        if 0 <= nro < len(self.hissit):
            self.hissit[nro].siirryKerrokseen(kohdekerros)
            print(f"Hissi {nro} saavutti kerroksen {kohdekerros}")
    def palohälytys(self):
        for h in range(self.hissienlkm):
            self.ajaHissiä(h, self.akerros)
        print("Palohälytys! Hissit siirretty pohjakerrokseen. ")

#talo1 = talo(-1,5, 2)
#talo1.luoHissit()

#talo1.ajaHissiä(1, 2)
#talo1.ajaHissiä(0, 4)

#h = hissi(-5, 5, 0)

#h.siirryKerrokseen(5)

#h.siirryKerrokseen(-3)