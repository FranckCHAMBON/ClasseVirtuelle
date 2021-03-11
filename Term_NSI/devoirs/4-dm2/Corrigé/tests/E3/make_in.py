from random import randrange
n = 300
print(n)
print(" ".join(map(str, (randrange(0, 10**9) for _ in range(n)))))
