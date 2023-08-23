lux = ("LUX on parvekkeellinen hytti yläkannella.")
a = ("A on ikkunallinen hytti autokannen yläpuolella.")
b = ("B on ikkunaton hytti autokannen yläpuolella.")
c = ("C on ikkunaton hytti autokannen alapuolella.")

luokka = input("Valitse hyttiluokka: ")

if luokka == "lux":
    print(lux)
elif luokka == "a":
    print(a)
elif luokka == "b":
    print(b)
elif luokka == "c":
    print(c)
else:
    print("Virheellinen hyttiluokka.")
