leiviska = int(8504)
naula = int(425)
luoti = int(13)
summa = int(0)
kilo = int(0)
gramma = int(0)

leiviskat = int(input("Anna leiviskat: " ))
naulat = int(input("Anna naulat: " ))
luodit = int(input("Anna luodit: " ))

summa = leiviskat * leiviska + naula * naulat + luoti * luodit

kilo = summa / 1000
gramma = summa % 1000
kilo = int(kilo)

print("Massa nykymittojen mukaan " + str(kilo) + " kilogrammaa ja " + str(gramma) + " grammaa.")


