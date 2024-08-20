from random import randint

c_choice = randint(1,10)
while True:
    p_choice = int(input("Numero 1-10 väliltä: "))

    if p_choice == c_choice:
        print("Voitit!")
        quit()

    elif p_choice > c_choice:
        print("Liian suuri arvaus. ")
    elif p_choice < c_choice:
        print("Liian pieni arvaus. ")