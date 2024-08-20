nums = []

while True:
    num = input("Numero: ")
    if num.strip(" ") == "":
        break
    num = int(num)
    nums.append(num)

nums.sort()

print(f"Isoin: {nums[-1]}\nPienin: {nums[0]}")