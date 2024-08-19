
leiviskat = float(input("Anna leiviskät.\n"))
naulat = float(input("Anna naulat.\n"))
luodit = float(input("Anna luodit.\n"))

print("Massa nykymittojen mukaan: ")
leiviskat_naulana = leiviskat * 20
kaikki_naulat = naulat + leiviskat_naulana
kaikki_luodit = kaikki_naulat * 32 + luodit
total = kaikki_luodit * 13.3 / 1000
b = str(total).split(".")
print(b[0], "kilogrammaa ja ", b[1], "grammaa.")