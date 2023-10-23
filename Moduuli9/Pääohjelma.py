import Autot
import Kilpailut
import random

#Kilpailuautojen lisääminen listaan
kilpailuAutot = []
kilpailuAutot.append(Autot.Auto("ABC-1", random.randint(100, 200)))
kilpailuAutot.append(Autot.Auto("ABC-2", random.randint(100, 200)))
kilpailuAutot.append(Autot.Auto("ABC-3", random.randint(100, 200)))
kilpailuAutot.append(Autot.Auto("ABC-4", random.randint(100, 200)))
kilpailuAutot.append(Autot.Auto("ABC-5", random.randint(100, 200)))
kilpailuAutot.append(Autot.Auto("ABC-6", random.randint(100, 200)))
kilpailuAutot.append(Autot.Auto("ABC-7", random.randint(100, 200)))
kilpailuAutot.append(Autot.Auto("ABC-8", random.randint(100, 200)))
kilpailuAutot.append(Autot.Auto("ABC-9", random.randint(100, 200)))
kilpailuAutot.append(Autot.Auto("ABC-10", random.randint(100, 200)))

# Luo polttomoottori-olion
polttomoottori = Autot.polttomoottori("ABC-Poltto", 200,  1, 50)

# Luo sähköauto-olion
sähköauto = Autot.sähköauto("DEF-Sähkö", 150, 2, 100)

# Kiihdytä autoja 100 kilometriin tunnissa
sähköauto.kiihdytäAutoa(100)
polttomoottori.kiihdytäAutoa(100)
# Käsketään luotuja autoja liikkumaan kolmen tunnin matka.
sähköauto.kuljeMatka(3)
polttomoottori.kuljeMatka(3)

print("Sähköauton matka: " + str(sähköauto.matka) + " kilometriä. " + "Polttomoottorin matka: " + str(polttomoottori.matka) + " kilometriä.")

# Lisätään autot Kilpailu luokkaan
suuriRomuralli = Kilpailut.kilpailu("Suuri romuralli", 8000, kilpailuAutot)
suuriRomuralli.lisääAutot(kilpailuAutot)
suuriRomuralli.kilpailuOhi()

# Kilpailu looppi

#index = int(0)
#autoMatka = 0
#loppu = False

#while loppu == False:
#    if index < len(kilpailuAutot):
#        kilpailuAutot[index].kiihdytäAutoa(random.randint(-10, 15))
#        kilpailuAutot[index].kuljeMatka(1)
        # print(str(kilpailuAutot[index].matka) + " " + kilpailuAutot[index].rekisteritunnus)

#    if kilpailuAutot[index].matka >= 10000:
#        loppu = True

#    elif index >= len(kilpailuAutot) - 1:
#        index = 0

#   else:
#        index += 1

#print("Voittaja on: " + kilpailuAutot[index].rekisteritunnus)

#print("Auton nimi: " + " Huippunopeus: ")
#print("--------------------------")

#for auto in kilpailuAutot:
#    print(auto.rekisteritunnus + "    |   " + str(auto.huippunopeus))

#    for auto in kilpailuAutot:
#        if auto.matka >= 10000:
#            autoMatka = 1
# print(f' Rekisteritunnus: {auto1.rekisteritunnus} \n Huippunopeus: {auto1.huippunopeus} \n Tämänhetkinen nopeus: {auto1.tnopeus} \n Kuljettu matka: {auto1.matka}')

#Tehtävä 2 ja 3
#auto1.kiihdytäAutoa(30)
#auto1.kiihdytäAutoa(70)
#auto1.kiihdytäAutoa(50)
#auto1.kiihdytäAutoa(-200)

#auto1.kiihdytäAutoa(50)

#auto1.kuljeMatka(float(input("Tuntimäärä: ")))