""" 
Prologin: Qualification 2003 
Exercice: 3 - Les trois nombres
https://prologin.org/train/2003/qualification/les_trois_nombres?fork=214068#submit
"""

""" 
L'algorithme détermine si un nombre parmis les 3 est égal à la somme des deux autres. 
La fonction renvoie ce nombre s'il existe, 0 sinon.

Exemple d'entrée:  18 42 24 
Exemple de sortie: 42 

Exemple d'entrée:  11 37 18 
Exemple de sortie: 0
"""

# tests 
import doctest 
doctest.testmod()

#Entrée
nombre = list(map(int, input().split()))

#Algorithme
for i in range(nombre): 
    if liste[2] == liste[0]+liste[1]: 
        print(liste[2]) #Sortie
    if liste[0]==liste[1] + liste[2]:
        print(liste[0]) #Sortie
    if liste[1]==liste[0] + liste[2]: 
        print(liste[1]) #Sortie
    else: 
        print("0") #Sortie


