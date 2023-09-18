class Kirja:
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        self.nimi = nimi

    def tulostaKirjanTiedot(self):
        print("Kirjan nimi: " + self.nimi + " | Kirjoittaja: " + self.kirjoittaja + " | Sivumäärä: " + str(self.sivumäärä))
class Lehti:
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        self.nimi = nimi
    def tulostaLehdenTiedot(self):
        print("Lehden nimi: " + self.nimi + " | Päätoimittaja: " + self.päätoimittaja)