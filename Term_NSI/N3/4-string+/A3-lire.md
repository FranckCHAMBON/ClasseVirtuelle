# [Lire ou ne pas lire, telle est (à nouveau) la question](http://www.france-ioi.org/algo/task.php?idChapter=556&iOrder=6)

## Sujet

Un des employés de la bibliothèque avait mis au point son propre algorithme de sélection des livres à lire, basé sur la longueur des titres des livres. Il s’en est lassé et se base maintenant sur l'ordre alphabétique des titres des livres.

Sur une étagère sont alignés tous les livres qui l’intéressent. Chaque mois, cette personne prend le premier livre de l’étagère, puis le second et ainsi de suite jusqu’à la fin. Seulement, elle ne lira un livre que si son titre est situé, selon l’ordre alphabétique, après chacun des livres qu’elle a lus pendant le mois. Si ce n’est pas le cas, elle enlève le livre de l’étagère, sans le lire.

Étant donnée la liste de titres de livres possibles pour le mois suivant, donnés dans l’ordre où ils apparaissent dans l’étagère, vous devez déterminer lesquels elle va lire.

### Contraintes

Chaque titre de livre contiendra au plus 100 caractères.

### Entrée

* Sur la première ligne, un entier `nbLivres`, le nombre total de livres.

* Les `nbLivres` lignes suivantes contiennent chacune un titre de livre.

* Les titres ne contiennent que des lettres majuscules ou des espaces.

### Sortie

* La liste des titres respectant la règle donnée dans l’énoncé.

### Exemple

---

entrée :

```
8
ANNA KARENINE
JACQUES LE FATALISTE ET SON MAITRE
DIX PETITS NEGRES
CENT ANS DE SOLITUDE
LA PESTE
LA FERME DES ANIMAUX
SUR LA ROUTE
SA MAJESTE DES MOUCHES
```

sortie :

```
ANNA KARENINE
JACQUES LE FATALISTE ET SON MAITRE
LA PESTE
SUR LA ROUTE
```

## Solution

```python
nb_livres = int(input())
livre_précédent = ""
for _ in range(nb_livres):
    livre = input()
    if livre > livre_précédent:
        print(livre)
        livre_précédent = livre
```

### Commentaire

* On initialise `livre_précédent = ""` ; cette chaîne de caractère est la plus petite de toute avec l'ordre alphabétique.
* On le met à jour quand on lit un nouveau livre.
