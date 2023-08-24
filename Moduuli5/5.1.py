import random

arpakuutiot = []
kysy = int(input("Syötä arpakuutioiden määrä: "))
summa = int(0)

while kysy > 0:
    arpakuutiot.append(0)
    kysy-=1

for a in arpakuutiot:
    a = random.randint(1,6)
    summa = summa + a
    print(summa)