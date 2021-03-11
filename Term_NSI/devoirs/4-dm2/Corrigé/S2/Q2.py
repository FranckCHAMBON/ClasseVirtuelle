"""
Prologin: Qualification 2003
Exercice: 2 - Comparer des chaines
https://prologin.org/train/2003/qualification/comparer_des_chaines/
"""

"""
Cette algorithme renvoie la première chaine de caractère selon l'ordre lexicographique (ordre du dictionnaire).

Exemple d'entrée:  8 
                   prologin 
                   5 
                   prolo 
Exemple de sortie: prolo 

Exemple d'entrée:  4 
                   toto 
                   4 
                   titi 
Exemple de sortie: titi

"""

# tests 
import doctest 
doctest.testmod()

#Entrée 
nb1_chaine_cara = int(input()) 
mot_1 = input() 
nb2_chaine_cara = int(input()) 
mot_2 = input() 

#Algorithme 
Liste =[mot_1,mot_2]
Liste_triée = sorted(Liste) 

#Sortie
print(Liste[0])
