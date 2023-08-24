lukuArray = []
suurin = int(0)
syote = "0"

while syote != "":
    syote = (input("Syötä luku: "))
    if syote != "":
        luku = int(syote)
        lukuArray.append(luku)
        lukuArray.sort(reverse=True)
        print(lukuArray)

while len(lukuArray) > 5:
    lukuArray.pop()

print(lukuArray)
