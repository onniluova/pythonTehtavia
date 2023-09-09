class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tnopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tnopeus = tnopeus
        self.matka = matka

    def kiihdytäAutoa(self, muutos):
        #if self.huippunopeus > self.tnopeus:
        self.tnopeus += muutos

        if  self.huippunopeus < self.tnopeus:
            self.tnopeus = self.huippunopeus

        if self.tnopeus < 0:
            self.tnopeus = 0

        #print(self.tnopeus)

    def kuljeMatka(self, tuntimaara):
            self.matka += tuntimaara * self.tnopeus
            #print(self.matka)