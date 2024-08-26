from calendar import isleap

vuosi = int(input("Anna vuosia: "))

if isleap(vuosi):
    print("Vuosi on karkausvuosi!")
else:
    print("Vuosi ei ole karkausvuosi!")