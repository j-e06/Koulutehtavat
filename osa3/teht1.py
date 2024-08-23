
min_pituus = 37

kalan_pituus = int(input("Anna kuhan pituus senttimetreinä: "))

if kalan_pituus < min_pituus:
    x = min_pituus - kalan_pituus
    print(f"heitä takas veteen, pitäs olla {x} cm pitempi")
else:
    print("kaikki ok")
