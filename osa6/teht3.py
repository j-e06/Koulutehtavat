def usa_bensa(bensiini_maara: int):
    return bensiini_maara * 3.785


while True:
    maara = int(input("Anna galloonia: "))
    if maara <= 0:
        print("Nähdään!")
        break
    print(usa_bensa(maara))