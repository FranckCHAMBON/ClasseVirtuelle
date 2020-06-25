def pe029(max_a=100, max_b=100):
    """
    Retourne le nombre d'éléments distincts dans
    a^b (a à la puissance b) pour
    * 2 <= a <= max_a
    * 2 <= b <= max_b

    >>> pe029(5, 5)
    15
    """

    """
    # méthode peu efficace avec les listes
    puissances = list()
    for a in range(2, max_a+1):
        for b in range(2, max_b+1):
            # ajouter (sans doublon) a**b dans l'ensemble des puissances
            puiss = a**b
            if (puiss not in puissances):
                puissances.append(puiss)
    return len(puissances)
    """

    # méthode efficace avec les ensembles
    puissances = set()
    for a in range(2, max_a+1):
        for b in range(2, max_b+1):
            # ajouter (sans doublon) a**b dans l'ensemble des puissances
            puiss = a**b
            puissances.add(puiss)
    return len(puissances)

assert pe029(5, 5) == 15

print(pe029())
