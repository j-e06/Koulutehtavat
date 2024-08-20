def placeholder(nums: list):
    total = 0
    for i in nums:
        total += i
    return total


test = [1,2,3,4,5,6,6,6,6]

print(placeholder(test))