sukupuoli = input("Syötä sukupuolesi (m/n): ")
hemoglobiini = int(input("Syötä hemoglobiiniarvot: "))

#Naisen hemoglobiinit
if sukupuoli == "n":
    if (hemoglobiini > 117 & hemoglobiini < 175):
        print("Hemoglobiiniarvot normaalit")

elif (hemoglobiini > 175):
    print("Hemoglobiiniarvot korkeat")

elif (hemoglobiini < 117):
    print("Hemoglobiiniarvot alhaiset")

#Miehen hemoglobiinit
if sukupuoli == "m":
    if (hemoglobiini > 134 & hemoglobiini < 195):
        print("Hemoglobiiniarvot normaalit")

elif (hemoglobiini > 195):
    print("Hemoglobiiniarvot korkeat")

elif (hemoglobiini < 134):
    print("Hemoglobiiniarvot alhaiset")