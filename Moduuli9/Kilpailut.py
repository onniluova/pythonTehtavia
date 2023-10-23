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

    def tulostaTilanne(self):
        print("Auton nimi: " + " Huippunopeus: ")
        print("--------------------------")
        autoMatka = int(0)
        for auto1 in self.osallistujat:
            print(auto1.rekisteritunnus + "    |   " + str(auto1.huippunopeus))
            print(f' Rekisteritunnus: {auto1.rekisteritunnus} \n Huippunopeus: {auto1.huippunopeus} \n Tämänhetkinen nopeus: {auto1.tnopeus} \n Kuljettu matka: {auto1.matka}')

    def kilpailuOhi(self):
        index = int(0)
        loppu = False
        tulostus = 0

        while loppu == False:
            if index < len(self.osallistujat):
                self.osallistujat[index].kiihdytäAutoa(random.randint(-10, 15))
                self.osallistujat[index].kuljeMatka(1)
                # print(str(kilpailuAutot[index].matka) + " " + kilpailuAutot[index].rekisteritunnus)
            if self.osallistujat[index].matka >= 8000:
                print("Voittajan kulkema matka: " + str(self.osallistujat[index].matka))
                loppu = True

            elif index >= len(self.osallistujat) - 1:
                tulostus += 1
                index = 0

            if tulostus == 10:
                self.tulostaTilanne()
                tulostus = 0
            else:
                index += 1

        print("Voittaja on: " + self.osallistujat[index].rekisteritunnus)