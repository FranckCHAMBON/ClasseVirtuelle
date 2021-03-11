"""
Prologin : Épreuve régionale 2003
Exercice : Le mot le plus long
https://prologin.org/train/2003/semifinal/mot_le_plus_long
"""

def mot_le_plus_long(chaine_caractère: str) -> int:
    """Cette fonction prend en paramètre une chaîne de caractère et renvoie le nombre de caractère du plus long mot de cette chaîne.
    >>> 74
        ecrivez une fonction qui trouve la longueur du plus long mot dans ce texte
    8
    """
    chaine_caractère = chaine_caractère.split()
    mot = ""
    for x in chaine_caractère:
        if len(mot) < len(x):
            mot = x
    return len(mot)


# Entrée
nb_caractère = int(input())
chaine_caractère = input()

# Sortie
print(mot_le_plus_long(chaine_caractère))