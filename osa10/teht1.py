class Hissi:
    def __init__(self, alin_kerros: int, ylin_kerros: int):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

        self.nykyinen_kerros = 0

    def siirry_kerrokseen(self, kerros:int):
        if self.nykyinen_kerros < kerros:
            while self.nykyinen_kerros < kerros:
                self.kerros_ylos()
        elif self.nykyinen_kerros > kerros:
            while self.nykyinen_kerros > kerros:
                self.kerros_alas()
        else:
            pass
    def kerros_ylos(self):
        if self.nykyinen_kerros != self.ylin_kerros:
            self.nykyinen_kerros += 1
            print("Nykyinen kerros: ",self.nykyinen_kerros)

    def kerros_alas(self):
        if self.nykyinen_kerros != self.alin_kerros:

            self.nykyinen_kerros -= 1
            print("Nykyinen kerros: ",self.nykyinen_kerros)


class Talo:
    def __init__(self, alin_kerros: int, ylin_kerros: int, hissien_maara:int):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_maara = hissien_maara
        self.hissit = {}
        for i in range(1,hissien_maara+1):
            self.hissit[i] = Hissi(alin_kerros, ylin_kerros)

        #for k,v in hissit.items():
        #    print(k,v.nykyinen_kerros, "\n")

    def aja_hissia(self,hissi_numero: int, kerros:int):
        if hissi_numero in self.hissit:
            if kerros == self.hissit[hissi_numero].nykyinen_kerros:
                pass
            else:
                self.hissit[hissi_numero].siirry_kerrokseen(kerros)

    def palohalytys(self):
        print("Tämä on palohälytys.")
        for hissi_numero, hissi in self.hissit.items():
            hissi.siirry_kerrokseen(self.alin_kerros)

#h = Hissi(alin_kerros=1, ylin_kerros=10)

#h.siirry_kerrokseen(5)
#h.siirry_kerrokseen(10)
#h.siirry_kerrokseen(1)

talo = Talo(1,10, 5)
print("-----\n")

talo.aja_hissia(1,10)
print("-----\n")
talo.aja_hissia(3, 5)
print("-----\n")
print(talo.aja_hissia(-11,10))

talo.palohalytys()
#for k,v in talo.hissit.items():
#    print(v.nykyinen_kerros)

