from itertools import zip_longest

def filtre_titre(titre: str, acronyme: str) -> str:
    """
    Renvoie une version capitalizée de titre,
    uniquement si elle correspond à l'acronyme,
    sinon la chaîne vide ''

    >>> filtre_titre("sALut toI", "ST")
    'Salut Toi'
    
    >>> filtre_titre("Autre chose", "AZERTY")
    ''

    """
    mots = list(titre.split())
    if all(mot[0].upper() == lettre 
            for mot, lettre in zip_longest(mots, acronyme, fillvalue=" ")):
                return " ".join(map(str.capitalize, mots))
    return '' # sinon
    

acronyme = input()
nb_titres = int(input())
for _ in range(nb_titres):
    titre = filtre_titre(input(), acronyme)
    if titre != '':
        print(titre)
