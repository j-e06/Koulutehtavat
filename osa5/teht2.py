nums = []

while True:

    entry = input("Anna numero: ")
    if entry == "":
        break
    nums.append(int(entry))

nums.sort(reverse=True)

for i in range(5):
    print(nums[i])