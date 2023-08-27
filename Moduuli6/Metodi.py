def palautaSumma(self):
        summa = int(0)
        for l in range(len(self)):
            summa = summa + (self[l])
        return print("Summa: " + str(summa))