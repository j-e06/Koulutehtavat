from random import randint
a = ''.join(str(randint(0,9)) for _ in range(1,4))
d = ''.join(str(randint(1,6)) for _ in range(1,5))

print(a, "\n"+ d)

