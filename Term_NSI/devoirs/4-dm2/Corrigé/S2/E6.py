"""
Prologin: Entraînement 2003
Exercice: 6 - Nombres impairs
https://prologin.org/train/2003/semifinal/nombres_impairs
"""
"""Cette algorithme deux entiers en paramètres, et il affiche, dans l'ordre croissant, tous les nombres impairs se trouvant entre ces deux entiers.
exemple d'entrée : 42 51
exemple de sortie : 43 45 47 49 51
                   
"""
# tests
import doctest
doctest.testmod()

# Entrée
nb_1, nb_2 = map(int, input().split())

# Algorithme
nb_impaire=[x for x in range(nb_1, (nb_2+1)) if x%2] #écriture fonctionnelle
résultat_conversion = ' '.join(str(elem) for elem in nb_impaire)  #Conversion d’une liste d'entiers en chaîne de caractère en utilisant join()

# Sortie
print(résultat_conversion)
