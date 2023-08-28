class pizza:
    hinta = int(10)
    halkasija = int(120)
def palautaPizza (halkaisija, hinta):
    neliometri = int(halkaisija * 10000)
    hinta = int(hinta / neliometri)
    return hinta

palautaPizza(pizza)