num = int(0)
pienin = int(0)
suurin = int(0)
syote = "0"

while syote != "":
    syote = (input("Syötä luku: "))
    if syote != "":
        num = int(syote)
        if num > suurin:
            suurin = num
        elif num < pienin:
            pienin = num

print("Suurin numero: " + str(suurin) + " pienin numero: " + str(pienin))