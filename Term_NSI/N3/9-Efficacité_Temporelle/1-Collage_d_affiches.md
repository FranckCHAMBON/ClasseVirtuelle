# [Collage d'affiches](http://www.france-ioi.org/algo/task.php?idChapter=528&iOrder=1)

Des affiches rectangulaires sont collées les unes après les autres sur un mur. Toutes les affiches ont la même largeur. On vous donne la hauteur `Hi` de chacune de ces affiches, dans l'ordre dans lequel elles sont collées. Le coin supérieur gauche de chaque affiche est toujours placé exactement sur le coin supérieur gauche du mur, et ce dernier est toujours plus grand que les affiches. Régulièrement, entre deux collages d'affiches, on vous demande d'indiquer combien d'affiches, parmi celles déjà collées, sont au moins en partie visibles, c'est à dire qu'une surface non nulle n'a été recouverte par aucune affiche collée depuis.

## Contraintes

* `1 <= nbRequetes <= 100 000`, où `nbRequetes` est le nombre de requêtes, une requête pouvant correspondre au collage d'une affiche ou bien à une question sur le nombre d'affiches visibles.
* `1 <= hauteuri <= 1 000 000`, où `hauteuri` est la hauteur d'une affiche.

### Entrée

La première ligne de l'entrée est constituée d'un unique entier : `nbRequetes`

Chacune des `nbRequetes` lignes suivantes commence par un caractère pouvant être 'Q' ou 'C'. Un caractère 'Q' correspond à la question : "Combien d'affiches sont actuellement visibles ?". Un caractère 'C' est suivi d'un entier hauteur et correspond au collage d'une affiche de hauteur `hauteur`.

### Sortie

La sortie de votre programme doit correspondre aux réponses aux questions données en entrée, dans l'ordre dans lequel elles apparaissent.

### Exemples

#### Exemple 1

entrée :

    12
    C 2
    Q
    C 4
    C 2
    Q
    C 9
    Q
    C 9
    C 2
    Q
    C 8 
    Q

sortie :

    1
    2
    1
    2
    2

#### Exemple 2

entrée :

    10
    Q
    C 8
    C 7
    C 11
    Q
    C 2
    C 4
    C 3
    Q
    C 3

sortie :

    0
    1
    3

