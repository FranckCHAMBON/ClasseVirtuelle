from random import randrange

L = H = 100

print(L, H)

grille = [['0' for _ in range(L)] for _ in range(H)]

for k in range(13):
    q = int(1.5**k)
    r = L//3 // q
    for _ in range(q):
        c_i = randrange(0, H)
        c_j = randrange(0, L)
        for i in range(1, H-1):
            for j in range(1, L-1):
                if (c_i - i)**2 + (c_j - j)**2 <= r**2:
                    grille[i][j] = "01"[k&1]

for ligne in grille:
    print("".join(ligne))
