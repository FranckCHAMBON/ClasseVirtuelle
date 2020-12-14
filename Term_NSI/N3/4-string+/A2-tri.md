# [Trier des livres](http://www.france-ioi.org/algo/task.php?idChapter=556&idTask=2423)

## Sujet

Un enfant un peu turbulent a complètement renversé une étagère pleine de livres ! Tous les livres sont désormais à terre, en vrac, et c’est à vous de tout remettre sur l’étagère dans le bon ordre.

À vous donc de trier ces livres par ordre alphabétique.

### Contraintes

Chaque titre de livre contient au plus 100 caractères.

### Entrée

* La première ligne contient un entier `nbLivres`, le nombre de livres.

* Les `nbLivres` lignes suivantes contiennent chacune un titre de livre.

* Les titres ne contiennent que des lettres majuscules ou des espaces.
Sortie

* L’ensemble des titres de livres, un titre par ligne, triés selon l’ordre alphabétique.

### Exemple

---

entrée :

```
7
LE ROUGE ET LE NOIR
DES SOURIS ET DES HOMMES
GUERRE ET PAIX
LE PARFUM
ALICE AU PAYS DES MERVEILLES
NOTRE DAME DE PARIS
LE VIEIL HOMME ET LA MER
```

sortie :


```
ALICE AU PAYS DES MERVEILLES
DES SOURIS ET DES HOMMES
GUERRE ET PAIX
LE PARFUM
LE ROUGE ET LE NOIR
LE VIEIL HOMME ET LA MER
NOTRE DAME DE PARIS
```

---

## Solution

```
nb_livres = int(input())
livres = [input() for _ in range(nb_livres)]

livres.sort()

for livre in livres:
    print(livre)
```

### Commentaire
* Python inclut une fonction de tri, et la comparaison des chaînes de caractères se fait suivant l'ordre alphabétique.
* On peut itérer sans indice pour la sortie.

