codes = {}

while True:
    first = input("Haluatko mennä olemassa olevaan lentokenttään vai uuteen? (uusi/vanha, q lopettaaksesi)")
    if first == "uusi":
        nimi = input("Lentokentän nimi: ")
        icao = input("ICAO koodi: ")

        codes[icao]=nimi
    elif first == "vanha":
        icao = input("ICAO koodi: ")
        print(codes[icao])
    elif first == "q":
        quit()
    else:
        print("miksi olet täällä?")