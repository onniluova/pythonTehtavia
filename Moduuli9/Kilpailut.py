import Autot
import random
class kilpailu:
    def __init__(self, nimi, pituus, osallistujat):
        self.nimi = nimi
        self.pituus = pituus
        self.osallistujat = []

    def lisääAutot(self, autot):
        for o in autot:
            self.osallistujat.append(o)
            print("Auto lisätty")
    def kilpailuOhi(self):
        index = int(0)
        loppu = False

        while loppu == False:
            if index < len(self.osallistujat):
                self.osallistujat[index].kiihdytäAutoa(random.randint(-10, 15))
                self.osallistujat[index].kuljeMatka(1)
                # print(str(kilpailuAutot[index].matka) + " " + kilpailuAutot[index].rekisteritunnus)

            if self.osallistujat[index].matka >= 10000:
                loppu = True

            elif index >= len(self.osallistujat) - 1:
                index = 0

            else:
                index += 1

        print("Voittaja on: " + self.osallistujat[index].rekisteritunnus)