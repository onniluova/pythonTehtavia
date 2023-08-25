import random
def palautaNoppa():
    noppa = int(0)

    while noppa != 6:
        noppa = random.randint(1, 6)
        print(noppa)

    return noppa