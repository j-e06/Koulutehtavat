def placeholder(halkaisija: float, hinta: float):
    from math import pi
    #Pinta-ala (ft2) = Pi x (halkaisija/2)^2
    test = pi * (halkaisija/2)**2
    return test / hinta

pitsa1_halkaisija = float(input("Pitsa 1 halkaisija: "))
pitsa1_hinta = float(input("Pitsa 1 hinta: "))

pitsa1 = placeholder(pitsa1_halkaisija, pitsa1_hinta)

pitsa2_halkaisija = float(input("Pitsa 2 halkaisija: "))
pitsa2_hinta = float(input("Pitsa 2 hinta: "))

pitsa2 = placeholder(pitsa2_halkaisija, pitsa2_hinta)
asd = pitsa2 - pitsa1
print(f"Pitsa {'1' if asd < 0 else '2'} on halvempi")