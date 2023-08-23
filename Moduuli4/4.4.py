import random

luku = int(random.randint(1, 10))
arvaus = int(0)

while arvaus != luku:
    arvaus = int(input("Arvaa luku: "))
    if arvaus < luku:
        print("Liian pieni arvaus")
    elif arvaus > luku:
        print("Liian suuri arvaus")

print("Oikein!")

