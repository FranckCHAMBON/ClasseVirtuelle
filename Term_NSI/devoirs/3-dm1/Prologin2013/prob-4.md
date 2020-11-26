# [Problème 4](https://prologin.org/train/2013/semifinal/gate_of_steiner)
> GATE OF STEINER

Niveau 2

## Énoncé

Tous les participants à GroLopin ont leur nom sur une carte !

Mais qui a obtenu le plus de lopins ? On vous donne la carte des joueurs, déterminer leur classement. En cas d'ex æquo, l'ordre importe peu (plusieurs réponses sont tolérées).

### Entrée

+ Sur la première ligne, deux nombres $N$ et $M$, respectivement la largeur et la longueur de la carte.
+ Sur les $N$ lignes suivantes : la carte de GroLopin. Une lettre minuscule représente un joueur, un `.` représente un lopin non acquis.

### Sortie

Sur une ligne, la chaîne formée des lettres minuscules, par ordre décroissant de nombre de lopins acquis.

### Contraintes

+ $1 \leqslant M, N \leqslant 500$

#### Contraintes d'exécution

+ Utilisation mémoire maximum : 1000 kilo-octets
+ Temps d'exécution maximum : 500 millisecondes

### Exemples d'entrée/sortie

---

Exemple d'entrée

    3 3
    aab
    bac
    cca

Exemple de sortie

    acb

---

Exemple d'entrée

    4 4
    a.ac
    .bab
    ..a.
    cccc

Exemple de sortie

    cab

---

## Indices

1. Il serait bon de préparer au moins deux fonctions (que nous avons déjà vues) : 
    + une fonction qui donne une lettre en fonction de son indice (de 0 à 25).
    + une fonction qui donne un indice (de 0 à 25) en fonction d'une lettre minuscule.

2. Enfin, il sera utile de trier un tableau de couple (lettre, quantité) avec la quantité comme critère... Nous avons déjà vu comment faire.

## Solution

*À venir*
