galloni = float(input("Syötä gallonit: "))

def muunnaLitroiksi(galloni):
    litrat = float(galloni * 0.379)
    print("Litroina: " + str(litrat))
    return litrat

muunnaLitroiksi(galloni)