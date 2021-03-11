"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/casse_tete_binaire
"""

BLANC = tuple([1]*16)

def lire():
    y = []
    for _ in range(4):
        for d in input()[:4]:
            assert d in "01"
            y.append(int(d))
    return tuple(y)


def change_1(i, j, x):
    y = list(x)
    k = 4*i + j
    y[k] = 1 - y[k]
    return tuple(y)

def change_ligne(i, x):
    y = list(x)
    i4 = i*4
    for j in range(4):
        y[i4 + j] = 1 - y[i4 + j]
    return tuple(y)

def change_colonne(j, x):
    y = list(x)
    for i in range(4):
        y[4*i+j] = 1-y[4*i+j]
    return tuple(y)

def rotation_gauche(i, x):
    y = list(x)
    i4 = i*4
    d = y[i4]
    y[i4] = y[i4  + 1]
    y[i4 + 1] = y[i4  + 2]
    y[i4 + 2] = y[i4  + 3]
    y[i4 + 3] = d
    return tuple(y)
    
def rotation_haut(j, x):
    y = list(x)
    d = y[j]
    y[j] = y[4 + j]
    y[4 + j] = y[8 + j]
    y[8 + j] = y[12 + j]
    y[12 + j] = d
    return tuple(y)

x = lire()
nb_coups = 0
vus = {x}
courant = {x}
while BLANC not in vus:
    nb_coups += 1
    suivant = set()
    for x in courant:
        #change 1
        for i in range(4):
            for j in range(4):
                y = change_1(i, j ,x)
                if y not in vus:
                    suivant.add(y)
                    vus.add(y)
        # change ligne
        for i in range(4):
            y = change_ligne(i ,x)
            if y not in vus:
                suivant.add(y)
                vus.add(y)
        # change colonne
        for j in range(4):
            y = change_colonne(j ,x)
            if y not in vus:
                suivant.add(y)
                vus.add(y)
        # rotation gauche
        for i in range(4):
            y = rotation_gauche(i ,x)
            if y not in vus:
                suivant.add(y)
                vus.add(y)
        # rotation haut
        for j in range(4):
            y = rotation_haut(j ,x)
            if y not in vus:
                suivant.add(y)
                vus.add(y)

    courant = suivant
print(nb_coups)
