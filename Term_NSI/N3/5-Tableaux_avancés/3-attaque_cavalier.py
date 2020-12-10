N = 8

def est_cavalier_blanc(case):
    return case == 'C'

def est_case_non_vide(case):
    return case != '.'

# les mouvements du cavalier
vecteurs = \
 [(1, 2), (2,1), (-1,2), (-2,1), (1,-2), (2,-1), (-1,-2), (-2,-1)]

# variante
vecteurs = [(1,2), (2, 1)]
vecteurs.extend([(-di, dj) for (di, dj) in vecteurs])
vecteurs.extend([(di, -dj) for (di, dj) in vecteurs])
assert len(vecteurs) == 8

def est_valide(i, j):
    return (0 <= i < N) and (0 <= j < N)

def est_noire(pièce):
    return 'a' <= pièce <= 'z'

def attaque_cavalier_blanc(échiquier):
    for i in range(N):
        for j in range(N):
            if est_cavalier_blanc(échiquier[i][j]):
                for di, dj in vecteurs:
                    idi, jdj = i + di, j + dj
                    if est_valide(idi, jdj):
                        menacée = échiquier[idi][jdj]
                        if est_case_non_vide(menacée):
                            if est_noire(menacée):
                                return True
    return False

# Lecture
échiquier = [input() for _ in range(N)]

# Écriture
print('yes' if attaque_cavalier_blanc(échiquier) else 'no')
