def somme_chiffres_puissances(b, e):
    """ Retourne la somme des chiffres de $b$ à la puissance $e$.
    Exemples :

    >>>somme_chiffres_puissances(2, 15)
    26
    >>>somme_chiffres_puissances(1, 15)
    1
    >>>somme_chiffres_puissances(10, 15)
    1
    """

    # première possibilité
    """
    n = b ** e
    # reste à trouver la somme des chiffres de n
    somme = 0
    while n != 0:
        n, unité = divmod(n, 10)
        somme += unité
    return somme
    """

    """
    # deuxième possibilité
    n = b ** e
    n_chaine = str(n)
    somme = 0
    for caractère in n_chaine:
        somme += int(caractère)
    return somme
    """
    

    # variante fonctionnelle
    return sum(map(int, str(b**e)))

assert somme_chiffres_puissances(2, 15) == 26

print(somme_chiffres_puissances(2, 1000))