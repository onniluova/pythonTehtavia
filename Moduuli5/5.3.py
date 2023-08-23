luku = int(input("Syötä luku: "))
laskuri = int(2)
eiole = bool(0)

while laskuri < luku:
    if luku % laskuri == 0:
        eiole = 1
        break
    laskuri+=1

if eiole == 0:
    print(str(luku) + " on alkuluku.")
else:
    print(str(luku) + " ei ole alkuluku.")