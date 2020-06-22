def valeur(ligne):
    """ Retourne la valeur d'un mot
    >>> valeur("COLIN")
    53
    """
    somme = 0
    for caractère in ligne:
        somme += ord(caractère) - ord("A") + 1
    return somme

assert valeur("COLIN") == 53


def pe022():
    """ Retourne la solution du problème 22 du projet Euler
    """

    
    with open("noms.txt", "r") as fichier_liste_noms:
        for ligne in fichier_liste_noms:
            prénoms = ligne.split(",")
    prénoms = [nom.strip('"') for nom in prénoms]
    prénoms.sort()

    somme = 0
    position = 0
    for ligne in prénoms:
        position += 1
        if position == 938:
            assert ligne == "COLIN", ("#"+ligne+"#")
        score = valeur(ligne) * position
        somme += score
    return somme

print(pe022())
