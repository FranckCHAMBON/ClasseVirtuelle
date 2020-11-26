# Devoir maison facultatif

Pour varier l'utilisation des juges en lignes, je vous propose [Prologin](https://prologin.org/).

En guise de devoir maison, je vous demande de faire des exercices parmi l'[entraînement régional 2013](https://prologin.org/train/2013/semifinal) ; dans l'ordre, autant que vous pouvez.

1. [La réponse à la question universelle](Prologin2013/prob-1.html)
2. [QI](Prologin2013/prob-2.html)
3. [XOR](Prologin2013/prob-3.html)
4. [GATE OF STEINER](Prologin2013/prob-4.html)
5. [Gravity](Prologin2013/prob-5.html)
6. [Reverse Alchemying](Prologin2013/prob-6.html)
7. [Échec et mat](Prologin2013/prob-7.html)

## Résolution

1. Vous pouvez vous inscrire sur Prologin ; c'est RGPD compatible, et c'est très sérieux.
2. Vous pouvez résoudre sur place les problèmes, ainsi vous saurez si vous avez réussi.
3. Pour chaque problème résolu (ou tenté), faire une sauvegarde du script dans un fichier nommé `problème_X.py` où `X` sera un chiffre entre `1` et `7`.

## Rendu du travail

1. Votre code sera noté sur sa réussite aux tests, mais aussi sur la qualité d'écriture.
2. Dans le site collaboratif ATRIUM Term_NSI, déposer vos fichiers dans le casier `DM prologin 2013`.
3. Les fichiers seront acceptés jusqu'au 29 novembre inclus.

## Conseils de rédaction

### Noms de variables
Il faut choisir de **meilleurs** noms de variables que ceux proposés dans l'énoncé.
Par exemple, le début du [problème 8](https://prologin.org/train/2013/semifinal/donjons_et_dragons) (qui n'est pas à faire) ne serait pas :

```python
P = int(input())
N, M = map(int,input().split())
for _ in range(M):
    a, b = map(int, input().split())
    #...
```

Mais plutôt :

```python
# 1. lecture de l'entrée
nb_points_vie = int(input())
nb_salles, nb_portes = map(int, input())

for _ in range(nb_portes):
    salle_a, salle_b = map(int, input().split())
    #...
```

On autorisera pour seules abréviations : 
* `nb` pour **nombre**
* `id` pour **identifiant**

On pourra omettre les articles :
* `de`, `du` ; ainsi **nombre de points de vie** devient `nb_points_vie`.
* `le`, `la` ; sauf s'ils sont important.

On pourra utiliser :
* `i`, `j` et `k` pour des coordonnées dans une grille, ou un **indice**.
    * `i` pour l'indice de ligne, `j` de colonne, et `k` autre indice.

### Fonctions
Écrire des fonctions,
* toujours avec *docstring*,
* souvent avec *doctest*,
* souvent avec annotation de type.
* inutile de faire une fonction `main()`

### Commentaires
Écrire des commentaires **avant** une phase de votre programme. Comme
```python
# 1. lecture de l'entrée
nb_points_vie = int(input())
```

### Respect de la PEP-8
Le PEP-8 devra être respectée le plus possible, sauf sur un point.
+ On préférera une utilisation correcte des accents dans les identifiants en français.

> Pour les autres : [rappel des bonnes pratiques](https://franckchambon.github.io/ClasseVirtuelle/Term_NSI/pep.html).


