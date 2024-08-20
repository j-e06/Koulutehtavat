class Auto:
    def __init__(self, rekisteritunnus: str, huippunomeus: int):
        self.rekitesteritunnus = rekisteritunnus

        self.huippunomeus = huippunomeus # given in km/h

        self.nykyinen_nopeus = 0

        self.kuljettu_matka = 0

    def kiihdytä(self, nopeus: int):
        print(nopeus, "asd \n")

        if nopeus > self.huippunomeus:
            pass
        elif nopeus < 0:
            if self.nykyinen_nopeus - nopeus < 0:
                print("hi")
                self.nykyinen_nopeus = 0
            else:
                self.nykyinen_nopeus = self.nykyinen_nopeus - nopeus
            pass


car = Auto("ABC-123", 142)

car.kiihdytä(30)
car.kiihdytä(70)
car.kiihdytä(50)
print(car.nykyinen_nopeus)
car.kiihdytä(-200)
print(car.nykyinen_nopeus)