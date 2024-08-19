sukupuoli = input("mikä on sinun biologinen sukupuoli? ")

hemoglobiarvo = int(input("mikä on sinun hemoglobiiniarvo? (pelkkä numero, ex 116)"))
alhainen = "hemoglobiarvo on alhainen"
normaali = "hemoglobiarvo on normaali"
korkea = "hemoglobiarvo on korkea"
if sukupuoli == "mies":
    if hemoglobiarvo < 134:
        print(alhainen)
    elif hemoglobiarvo > 195:
        print(korkea)
    else:
        print(normaali)
elif sukupuoli == "nainen":
    if hemoglobiarvo < 117:
        print(alhainen)
    elif hemoglobiarvo > 175:
        print(korkea)
    else:
        print(normaali)