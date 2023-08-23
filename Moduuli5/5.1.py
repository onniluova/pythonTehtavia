import random

arpakuutiot = [1, 1, 1, 1]
summa = int(0)

for a in arpakuutiot:
    a = random.randint(1,6)
    summa = summa + a
    print(summa)