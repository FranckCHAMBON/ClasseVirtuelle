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

+ Par tradition, on note $(i, j)$ les coordonnées dans une grille (ou une matrice), avec $i$ l'indice de ligne, et $j$ celui de colonne. Dans l'exemple précédent, il y a deux reines, une en $(1, 1)$, l'autre en $(4, 5)$. La case $(0, 0)$ correspond au coin supérieur gauche. Si on tourne la tête de $90°$, cela correspond à abscisse et ordonnée.
+ On pourra créer une fonction `est_valide(i, j)` qui renvoie un booléen : si la case de coordonnées $(i, j)$ est bien dans l'échiquier.
+ Ce problème est plus simple que le précédent !

## Solution

*À venir*
