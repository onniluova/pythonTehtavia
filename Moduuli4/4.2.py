cm = int(1)

while (cm > 0):
    cm = float(input("Syötä senttimetrit: "))
    tuuma = float(cm * 0.254)
    print("Tuumina: " + str(tuuma))