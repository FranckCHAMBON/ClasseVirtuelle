# Devoir maison obligatoire

> À rendre avant le dimanche 28 février 23h59 sur ATRIUM dans le casier `DM1_Prologin` du site collaboratif `1ère_NSI` : aller dans document, et vous verrez le casier. [Lien direct](https://www.atrium-sud.fr/group/1ere_nsi-395127/documents)
> * Seul le travail rendu **avant la limite** sera corrigé.
> * **Un seul** fichier sera lu par le professeur, le dernier avant la date.


## Questions de dernières minutes
* Il est totalement interdit de rendre un fichier `Word`, il ne sera pas lu.
    * Vous devez rendre des fichiers texte avec l'extension `.py`, tous archivés dans un fichier `.zip`
    * Un fichier `word` ne sera pas regardé ; du tout. En aucun cas.
* VSCodium n'est pas obligatoire pour fabriquer les fichiers `.py`.
    * Il est aussi possible d'utiliser [Geany](https://www.geany.org/download/releases/), ou tout autre éditeur de texte. (`Word` n'est pas un éditeur de texte !)
* Si vous rendez votre travail en retard, il y aura trois points par jour de pénalité ; tout jour entamé étant compté.
    * La notation est généreuse, il vaut mieux rendre un travail avec deux jours de retard, plutôt qu'avoir zéro pour travail non rendu !

## Sujet
* Résoudre les problèmes pour la session 2003 de Prologin.
    * [10 problèmes d'entraînement de niveau 0 à 3.](https://prologin.org/train/2003/semifinal)
    * [**Bonus facultatif**] : [4 problèmes de qualification de niveau 2](https://prologin.org/train/2003/qualification) ; attention, le premier est plus difficile que les autres...

* Écrire un code propre respectant les règles vues en classe.

* Votre travail doit être strictement personnel ; **toute trace de plagiat sera sanctionnée !**

* Créer une **unique** archive `.zip` contenant **toutes** vos solutions.
    * Le nom de l'archive sera `DM_Prologin_2003.zip`.
        * Inutile d'ajouter votre nom ou la date à ce fichier, ATRIUM le fera automatiquement.
    * Les fichiers inclus seront nommés :
        * `E1-42.py` pour le premier de l'entraînement,
        * `E2-Escalier.py`, `E3-Grand_écart.py`, etc pour les suivants.
        * `Q1-Cases_inaccessibles.py` pour le premier des qualifications,
        * et ainsi de suite, `Q<numéro>-<Nom_du_problème>.py`, **les espaces remplacées par tiret bas**.
    * Les fichiers seront tous de la forme donnée en exemple, avec :
        * Une entête personnalisée :
            * Avec votre nom et prénom.
            * `Prologin: Entraînement 2003` ou bien `Prologin: Qualification 2003`.
            * Le numéro et le titre du problème.
            * Le lien internet du problème.

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
    """
    ...# code à compléter



# Entrée
nb_lignes, nb_colonnes = map(int, input().split())
cases = [list(map(int, input().split())) for _ in range(nb_lignes)]

# Sortie
print(nb_cases_inaccessibles(nb_lignes, nb_colonnes, cases))

```

