def est_vide(arbre):
    return arbre is None

def somme(arbre):
    """On suppose ici que l'arbre binaire ne comporte
    que des valeurs numériques."""
    if est_vide(arbre):
        return 0
    else:
        return somme(arbre[0]) + arbre[1] + somme(arbre[2])

def taille(arbre):
    if est_vide(arbre):
        return 0
    else:
        return taille(arbre[0]) + taille(arbre[2])

def hauteur(arbre):
    if est_vide(arbre):
        return 0
    else:
        return max(taille(arbre[0]) + taille(arbre[2]))

def est_peigne_gauche(arbre):
    if est_vide(arbre):
        return True
    else:
        return est_peigne_gauche(arbre[0]) and est_vide(arbre[2])
