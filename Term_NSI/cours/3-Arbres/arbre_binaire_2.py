class Nœud:
    def __init__(self, gauche, élément, droite):
        self.gauche = gauche
        self.élément = élément
        self.droite = droite


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
        return 1 + max(taille(arbre.gauche) + taille(arbre.droite))

def est_peigne_gauche(arbre):
    if est_vide(arbre):
        return True
    else:
        return est_peigne_gauche(arbre.gauche) and est_vide(arbre.droite)
