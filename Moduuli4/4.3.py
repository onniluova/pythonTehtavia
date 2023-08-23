num = int(0)
pienin = int(0)
suurin = int(0)

while num != "":
    num = int(input("Syötä luku: "))
    if num > suurin:
        suurin = num
    elif num < pienin:
        pienin = num

print("Suurin numero: " + str(suurin) + " pienin numero: " + str(pienin))