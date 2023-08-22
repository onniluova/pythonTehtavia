leiviska = int(8504)
naula = int(425)
luoti = int(13)
summa = int(0)
kilo = int(0)

leiviskat = int(input("Anna leiviskat: " ))
naulat = int(input("Anna naulat: " ))
luodit = int(input("Anna luodit: " ))

summa = leiviskat * leiviska + naula * naulat + luoti * luodit

while summa > 1000:
    kilo+=1
    summa-=1000

print("Massa nykymittojen mukaan " + str(kilo) + " kilogrammaa ja " + str(summa) + " grammaa.")



