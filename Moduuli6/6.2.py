import random

tahkot = int(input("Syötä maksimisilmäluku: "))
def palautaNoppa(tahkot):
        noppa = int(0)
        while noppa < tahkot:
            noppa = int(random.randint(1, tahkot))
            print(noppa)
        return noppa

palautaNoppa(tahkot)