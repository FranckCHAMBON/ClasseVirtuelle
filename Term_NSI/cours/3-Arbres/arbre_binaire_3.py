import collections
Nœud = collections.namedtuple('Nœud', ['gauche', 'élément', 'droite'])


def est_vide(arbre):
    return arbre is None

def somme(arbre):
    """On suppose ici que l'arbre binaire ne comporte
    que des valeurs numériques."""
    if est_vide(arbre):
        return 0
    else:
        return somme(arbre.gauche) + arbre.élément + somme(arbre.droite)

def taille(arbre):
    if est_vide(arbre):
        return 0
    else:
        return taille(arbre.gauche) + 1 + taille(arbre.droite)

def hauteur(arbre):
    if est_vide(arbre):
        return 0
    else:
        return 1 + max(hauteur(arbre.gauche), hauteur(arbre.droite))

def est_peigne_gauche(arbre):
    if est_vide(arbre):
        return True
    else:
        return est_peigne_gauche(arbre.gauche) and est_vide(arbre.droite)

if __name__ == '__main__':
    # test
    six_1 = Nœud(None, "6", None)
    cinq_1 = Nœud(None, "5", None)
    produit_1 = Nœud(six_1, "×", cinq_1)

    trois_1 = Nœud(None, "3", None)

    sept_1 = Nœud(None, "7", None)
    six_2 = Nœud(None, "6", None)
    somme_1 = Nœud(sept_1, "+", six_2)

    somme_2 = Nœud(trois_1, "+", somme_1)
    expr_A = Nœud(produit_1, "-", somme_2)

    assert taille(expr_A) == 9
    assert hauteur(expr_A) == 4, hauteur(expr_A)

    assert not est_peigne_gauche(expr_A) # Il y a un not !!!
    assert est_peigne_gauche(trois_1) # comme toute feuille
