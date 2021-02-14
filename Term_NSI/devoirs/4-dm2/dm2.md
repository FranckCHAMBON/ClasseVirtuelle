# Devoir maison n°2

> À rendre avant le dimanche 28 février 23h59 sur ATRIUM dans le casier `Prologin_2003`.
> * Seul le travail rendu **avant la limite** sera corrigé.
> * **Un seul** fichier sera lu par le professeur, le dernier avant la date.

## Sujet
* Résoudre les problèmes pour la session 2003 de Prologin.
    * [4 problèmes de qualification de niveau 2.](https://prologin.org/train/2003/qualification)
    * [13 problèmes d'entraînement de niveau 0 à 4.](https://prologin.org/train/2003/semifinal)

* Écrire un code propre respectant les règles vues en classe.

* Votre travail doit être strictement personnel ; **toute trace de plagiat sera sanctionnée !**

* Créer une **unique** archive `.zip` contenant **toutes** vos solutions.
    * Le nom de l'archive sera `DM_Prologin_2003.zip`.
        * Inutile d'ajouter votre nom ou la date à ce fichier, ATRIUM le fera automatiquement.
    * Les fichiers inclus seront nommés :
        * `Q1-Cases_inaccessibles.py` pour le premier des qualifications,
        * et ainsi de suite, `Q<numéro>-<Nom_du_problème>.py`, **les espaces remplacées par tiret bas**,
        * `E1-42.py` pour le premier de l'entraînement,
        * `E2-Escalier.py`, `E3-Grand_écart.py`, etc pour les suivants.
    * Les fichiers seront tous de la forme donnée en exemple, avec :
        * Une entête personnalisée :
            * Avec votre nom et prénom.
            * `Prologin: Qualification 2003` ou bien `Prologin: Entraînement 2003`
            * Le numéro et le titre du problème.
            * Le lien internet du problème.
        * Une ou plusieurs fonctions pour résoudre le problème :
            * Avec `doctest` dès que possible.
        * Un bloc final qui lance les tests, puis qui gère l'entrée et la sortie du problème.

> Exemple de fichier `Q1-Cases_inaccessibles.py` :

```py
"""
Nom:
Prénom:
Prologin: Qualification 2003
Exercice: 1 - Cases inaccessibles
https://prologin.org/train/2003/qualification/cases_inaccessibles
"""

def nb_cases_inaccessibles(nb_lignes: int, nb_colonnes: int, cases: list) -> int:
    """Renvoie le nombre de cases inaccessibles suivant l'énoncé.
    
    >>> nb_lignes, nb_colonnes = 4, 3
    >>> cases = [[4, 5, 3], [3, 2, 6], [4, 1, 1], [0, 1, 2]]
    >>> nb_cases_inaccessibles(nb_lignes, nb_colonnes, cases)
    5
    
    """
    ...


# tests
import doctest
doctest.testmod()

# Entrée
nb_lignes, nb_colonnes = map(int, input().split())
cases = [list(map(int, input().split())) for _ in range(nb_lignes)]

# Sortie
print(nb_cases_inaccessibles(nb_lignes, nb_colonnes, cases))

```

