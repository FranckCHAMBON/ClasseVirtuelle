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
        return taille(arbre[0]) + 1 + taille(arbre[2])

def hauteur(arbre):
    if est_vide(arbre):
        return 0
    else:
        return 1 + max(hauteur(arbre[0]), hauteur(arbre[2]))

def est_peigne_gauche(arbre):
    if est_vide(arbre):
        return True
    else:
        return est_peigne_gauche(arbre[0]) and est_vide(arbre[2])


if __name__ == '__main__':
    # test
    six_1 = (None, "6", None)
    cinq_1 = (None, "5", None)
    produit_1 = (six_1, "×", cinq_1)

    trois_1 = (None, "3", None)

    sept_1 = (None, "7", None)
    six_2 = (None, "6", None)
    somme_1 = (sept_1, "+", six_2)

    somme_2 = (trois_1, "+", somme_1)
    expr_A = (produit_1, "-", somme_2)

    assert taille(expr_A) == 9
    assert hauteur(expr_A) == 4, hauteur(expr_A)

    assert not est_peigne_gauche(expr_A) # Il y a un not !!!
    assert est_peigne_gauche(trois_1) # comme toute feuille
