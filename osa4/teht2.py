
ratio = 2.54 # 1 tuuma = 2,54 cm

while True:
    maara = input("Anna tuumia: (tyhjä lopettaaksesi.) ")
    if maara.strip(" ") == "":
        quit()
    print(ratio * int(maara))