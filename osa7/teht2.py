names = set()
while True:
    name = input("Name: ")
    if name == "":
        break
    elif name in names:
        print("Existing name")
    else:
        names.add(name)
        print("New name")


for n in names:
    print(n)