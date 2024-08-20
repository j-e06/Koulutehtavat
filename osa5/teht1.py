from random import randint
maara = int(input("Arpakuutioiden lukumäärä: "))
count = 0
for i in range(maara):
    count += randint(1,6)

print(count)