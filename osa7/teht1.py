seasons = ("spring", "summer", "autumn", "winter")

kuukausi = int(input("Anna kuukauden numero: "))
if kuukausi < 0 or kuukausi > 12:
    quit()
if kuukausi == 12 or kuukausi <=2:
    print(seasons[3])
elif 3 <= kuukausi <= 5:
    print(seasons[0])
elif 6 <= kuukausi < 9:
    print(seasons[1])
elif 9 <= kuukausi < 12:
    print(seasons[2])
#huonosti tehty mutta meh toimii kuiteski


