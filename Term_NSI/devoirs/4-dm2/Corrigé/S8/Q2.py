"""
Prologin : Qualification 2003
Exercice : Comparer des chaînes
https://prologin.org/train/2003/qualification/comparer_des_chaines
"""

def comparaison_alphabétique(nb_caractère1: int, chaîne1: str, nb_caractère2: int, chaîne2: str) -> str:
    """Cette fonction prend en paramètre deux chaînes de caractères composées uniquement de lettre minuscules 
    et sans accents ainsi que le nombre de caractère, et renvoie la première selon l'odre lexicographique.
    >>> 8
        prologin
        5
        prolo
    prolo
    """
    nb_caractère_min = 0
    if nb_caractère1 < nb_caractère2:
        nb_caractère_min = nb_caractère1
    else:
        nb_caractère_min = nb_caractère2
    for x in range(nb_caractère_min):
        if x + 1 == nb_caractère_min:
            if chaîne1[x] < chaîne2[x]:
                return chaîne1 
            else:
                return chaîne2
        if chaîne1[x] == chaîne2[x]:
            pass
        else:
            if chaîne1[x] < chaîne2[x]:
                return chaîne1 
            else:
                return chaîne2
   

# Entrée
nb_caractère1 = int(input())
chaîne1 = input()
nb_caractère2 = int(input())
chaîne2 = input()
# Sortie
print(comparaison_alphabétique(nb_caractère1, chaîne1, nb_caractère2, chaîne2))