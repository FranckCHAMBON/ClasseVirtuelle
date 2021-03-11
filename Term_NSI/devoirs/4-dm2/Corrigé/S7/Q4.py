""" 
Prologin: Qualification 2003
Exercice: 4 - Nombre_de_voyelles
https://prologin.org/train/2003/qualification/nombre_de_voyelles
"""
def nombre_de_voyelles(chaîne_caractères:str)-> int:
    """ Prend une chaîne de caractères puis renvoie le nombres de voyelles présent dedans
    >>> nombre_de_voyelles("Je voudrais une bonne note en NSI")
    13
    >>> nombre_de_voyelles("Marseille est en France")
    8
    """

    # On transforme cette chaine de caractères en une liste de caractères.
    liste_caractères = list(chaîne_caractères)

    def est_voyelle(lettre:str) -> bool:
        """ 
        >>> est_voyelle("a")
        True
        >>> est_voyelle("X")
        False
        >>> est_voyelle("Y")
        True
        >>> est_voyelle("z")
        False
   
        """
        # On met tout en minuscule.
        lettre = lettre.lower()
        
        voyelles = {"a","e","i","o","u","y"}
        return lettre in voyelles


    nb_voyelles = 0
    for x in range(len(liste_caractères)):
        if est_voyelle(liste_caractères[x]):
            nb_voyelles += 1
    return nb_voyelles

# tests
import doctest
doctest.testmod()

# Entrée
nb_caractères = int(input())
chaîne_caractères = input()

# Sortie
print(nombre_de_voyelles(chaîne_caractères))



        
        

