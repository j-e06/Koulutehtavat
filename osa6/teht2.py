# kopioitu teht1.py

def random_noppa(faces):
    from random import randint
    return randint(1,faces)


max_amount = int(input("Mikä on maximi numero: "))
while True:
    num = random_noppa(max_amount)
    print(num)
    if num == max_amount:
        break
    else:
        continue

