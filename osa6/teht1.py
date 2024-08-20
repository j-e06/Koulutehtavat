def random_noppa():
    from random import randint
    return randint(1,6)


while True:
    num = random_noppa()
    print(num)
    if num == 6:
        break
    else:
        continue

