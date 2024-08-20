

username = "python"
password = "rules"

attempt_count = 0
while True:
    if attempt_count >= 5:
        print("Liian monta yritystä.")
        quit()
    name = input("Käyttäjätunnuksesi: ")
    word = input("Salasanasi: ")
    if name == username and word == password:
        #both correct
        print("Tervetuloa!")
        break
    else:
        print("Pääsy evätty.")

    attempt_count +=1