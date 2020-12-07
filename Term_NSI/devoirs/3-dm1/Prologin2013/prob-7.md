# [Problème 7](https://prologin.org/train/2013/semifinal/echec_et_mat)
>Échec et mat

Niveau 3

## Énoncé

Joseph Marchand est en train d'apprendre à jouer aux échecs en compagnie de son ami Garry Kasparov. Afin de vérifier si Joseph a bien compris comment se déplace une reine, Garry place $N$ reines sur un échiquier et lui demande combien il y a de cases qu'aucune reine ne peut atteindre en un seul tour de jeu. Vous devez réaliser pour lui un programme qui se charge de trouver la réponse afin de vérifier celle de Joseph.

On rappelle qu'un échiquier est composé de $8 × 8 = 64$ cases. Une reine peut se déplacer en ligne droite, verticalement, horizontalement, et diagonalement, d'autant de cases qu'elle le veut.

### Entrée

L'entrée standard contient l'échiquier. `.` représente une case libre et `X` représente une case occupée par une reine.

### Sortie

Le nombre de cases qu'aucune reine ne peut atteindre en un seul tour de jeu.

### Contraintes

+ $0 \leqslant N \leqslant 64$ où $N$ est le nombre de reines.

#### Contraintes d'exécution

+ Utilisation mémoire maximum : 100 kilo-octets
Temps d'exécution maximum : 200 millisecondes

### Exemples d'entrée/sortie

---

Exemple d'entrée

    ........
    ........
    ........
    ........
    ...X....
    ........
    ........
    ........

Exemple de sortie

    36

Commentaire : Les déplacements possibles de la dame sont ici indiqués par des x minuscules :

    ...x...x
    x..x..x.
    .x.x.x..
    ..xxx...
    xxxXxxxx
    ..xxx...
    .x.x.x..
    x..x..x.

Il reste donc 36 cases libres.

---

Exemple d'entrée

    ........
    .X......
    ........
    ........
    ...X....
    ........
    ........
    ........

Exemple de sortie

    20

---

## Indices

+ Par tradition, on note $(i, j)$ les coordonnées dans une grille (ou une matrice), avec $i$ l'indice de ligne, et $j$ celui de colonne. Dans l'exemple précédent, il y a deux reines, une en $(1, 1)$, l'autre en $(4, 3)$. La case $(0, 0)$ correspond au coin supérieur gauche. Si on tourne la tête de $90°$, cela correspond à abscisse et ordonnée.
+ On pourra créer une fonction `est_valide(i, j)` qui renvoie un booléen : si la case de coordonnées $(i, j)$ est bien dans l'échiquier.
+ On pourra créer une fonction `marque(i_0, j_0)` qui modifie une grille en marquant les cases menacées par une reine placée en $(i_0, j_0)$.
+ Ce problème est plus simple que le précédent !

## Solution

```python
"""
auteur : Franck CHAMBON
Régional 2013 - Problème 7 - Échec et mat
https://prologin.org/train/2013/semifinal/echec_et_mat
"""

def est_valide(i: int, j: int) -> bool:
    """Renvoie un booléen : (i, j) est-il dans la grille 8×8?
    Les coordonnées vont de 0 à 7.
    >>> est_valide(2, 5)
    True
    >>> est_valide(5, 8)
    False
    >>> est_valide(-2, 5)
    False
    """
    return (0 <= i < 8) and (0 <= j < 8)

def marque(i_0: int, j_0: int) -> None:
    """Modifie la grille, en marquant les cases menacées
    par une reine placée en (i_0, j_0).
    """
    # on marque la colonne j_0
    for i in range(8):
        if grille[i][j_0] == '.':
            grille[i][j_0] = 'x'

    # on marque la ligne i_0
    for j in range(8):
        if grille[i_0][j] == '.':
            grille[i_0][j] = 'x'
    
    # on marque une diagonale
    for k in range(-7, 8):
        i = i_0 + k
        j = j_0 + k
        if est_valide(i, j):
            if grille[i][j] == '.':
                grille[i][j] = 'x'

    # on marque l'autre diagonale
    for k in range(-7, 8):
        i = i_0 + k
        j = j_0 - k
        if est_valide(i, j):
            if grille[i][j] == '.':
                grille[i][j] = 'x'


# 1. lecture de l'entrée
grille = [list(input()) for _ in range(8)]

# 2. on marque les cases menacées
for i in range(8):
    for j in range(8):
        if grille[i][j] == 'X':
            marque(i, j)

# 3. on compte les cases non menacées
ans = 0
for i in range(8):
    for j in range(8):
        if grille[i][j] == '.':
            ans += 1
print(ans)
```
