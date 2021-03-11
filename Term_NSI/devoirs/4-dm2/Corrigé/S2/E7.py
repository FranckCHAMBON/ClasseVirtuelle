"""
Prologin: Entraînement 2003
Exercice: 7 - Table de multiplication
https://prologin.org/train/2003/semifinal/table_de_multiplications/210827
"""

"""Cette algorithme prend en paramètre un chiffre (entre 1 et 9), et il affiche la table de multiplication de ce chiffre.
exemple d'entrée : 3
exemple de sortie : 3x1=3
                    3x2=6
                    3x3=9
                    3x4=12
                    3x5=15
                    3x6=18
                    3x7=21
                    3x8=24
                    3x9=27
"""

# tests
import doctest
doctest.testmod()


# Entrée
nombre = int(input())

# Algorithme
for i in range(1,10):
    print(nombre,"x",i,"=",i*nombre,sep="") # Sortie