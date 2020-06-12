from math import gcd

def est_triplet(a, b, c):
    """
    Retourne Vrai ou Faux suivant que
    (a,b,c) sont les côtés entiers d'un triangle rectangle
    avec c l'hypothénuse et
    a² + b² = c²
    """
    return  a*a + b*b == c*c
    

quantité = 0
limite = 1000
for c in range(1, limite):
    for b in range(1, c):
        for a in range(1, b):
            if est_triplet(a, b, c):
                if gcd(a, b) == 1:
                    print(a, b, c)
                    quantité = quantité + 1

print("le nombre de triplets pythagoriciens est", quantité)
