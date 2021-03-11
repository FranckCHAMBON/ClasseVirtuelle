import time 
now = time.time()

"""
Nom: PALAZON
Prénom: Anabel
Prologin: Qualification 2003
Exercice: 8 - Puissance 4
https://prologin.org/train/2003/semifinal/puissance_4
"""

def résultat_p4(plateau : list) -> int :
    """ Renvoie 1 si le joueur aux pions jaunes a gagné la parti de puissance 4 
    (= 4 pions alignés à l'horizontale, verticale ou diagonale),
    2 si le gagnat est celui aux pions rouge, ou 0 si personne n'a gagné.
    Le 'plateau' est un tableau d'entiers de 42 cases (6 lignes, 7 colonnes) 
    contenants 0 si la case est vide, 1 s'il y a un pion est jaune, ou 2 s'il y a un pion rouge. 
    
    >>> plateau = [[0, 0, 1, 0, 0, 0, 0], \
                   [0, 0, 2, 2, 0, 0, 0], \
                   [0, 1, 2, 1, 0, 0, 0], \
                   [0, 2, 2, 1, 0, 0, 0], \
                   [2, 2, 1, 2, 1, 0, 0], \
                   [1, 2, 1, 1, 2, 1, 0]]
    >>> résulat_p4(plateau)
    2
    
    """
    aligné_jaune = 0
    aligné_rouge = 0
    for ligne in plateau :
        for case in lignes :
            if case == 1 :
                aligné_j += 1






# Initiation
nb_lignes, nb_colonnes, = 6, 7

# Entrée
plateau = [list(map(int, input().split()) for _ in range (nb_lignes))]

# Sortie
print (résultat_p4(plateau))