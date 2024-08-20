def placeholder(nums: list):
    return [i for i in nums if i % 2 == 0]


old = [1,2,3,4,5,7,8,9,10]

new = placeholder(old)
print(old)
print(new)