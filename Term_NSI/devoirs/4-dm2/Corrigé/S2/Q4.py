"""
Prologin:Qualification 2003
Exercice: 4- nombre_de_voyelles
https://prologin.org/train/2003/qualification/nombre_de_voyelles
"""

""" Cette fonction renvoie renvoie le nombre de voyelles du mot.
Exemple d'entrée : 8 
                   ProlOgiN 
Exemple de sortie: 3
"""



# tests 
import doctest 
doctest.testmod()

#Entrée
nb_caractère= int(input())
mot = input().lower() 

#Programme
voyelles = "aeiouy" 
fonction_nb_voyelles = sum(mot.count(i) for i in voyelles) 

#Sortie
print(fonction_nb_voyelles)

