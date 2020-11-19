# [Conditions avancées, opérateurs booléens](http://www.france-ioi.org/algo/chapter.php?idChapter=648)

> Correction alternative de certains problèmes

## Espion étranger

### Sujet

On vous donne un intervalle de temps pendant lequel on sait qu'un espion est arrivé, puis la date d'arrivée d'un certain nombre de personnes. Déterminez combien de ces personnes peuvent être cet espion.

Votre programme doit d'abord lire deux entiers : la date de début et la date de fin de l'intervalle pendant lequel on sait que l'espion est arrivé en ville. Il doit ensuite lire un entier nbEntrées, le nombre total de personnes entrées dans la ville, puis les nbEntrées nombres suivants qui représentent les dates d'entrée (non triées) des différentes personnes.

Votre programme doit afficher le nombre de personnes entrées entre les deux dates données, incluses.

### Exemple

entrée :

    6
    10
    5
    7
    11
    8
    3
    6

sortie :

    3

### Solution officielle

```python
dateDébut = int(input())
dateFin = int(input())
nbEntrées = int(input())
nbPersonnes = 0
for loop in range(nbEntrées):
   date = int(input())
   if dateDébut <= date and date <= dateFin:
      nbPersonnes = nbPersonnes + 1
print(nbPersonnes)
```

### Solution alternative

```python
date_début = int(input())
date_fin = int(input())
nb_entrées = int(input())
dates = iter(int(input()) for _ in range(nb_entrées))

nb_suspects = sum(1 for date in dates if date_début <= date <= date_fin)
print(nb_suspects)
```

Remarques
: La construction avec `iter` est presque équivalente à la création d'une liste avec `list` à la place ou bien `dates = [int(input()) for ...]`. La différence essentielle, est que la liste n'est pas créée effectivement en mémoire, juste elle est prête à être déroulée à la demande, une seule fois !
: `sum(1 for ... if ...)` est une construction qui permet de compter le nombre d'éléments satisfaisant un critère.

On peut aussi écrire avec un style encore plus fonctionnel.

```python
est_suspect = lambda date: date_début <= date <= date_fin
nb_suspects = sum(1 for _ in filter(est_suspect, dates))
```


## Maison de l'espion

### Sujet

 On vous décrit une zone de recherche rectangulaire, parallèle aux axes, puis la position d'un certain nombre de maisons. Écrivez un programme qui détermine combien de maisons sont dans cette zone.

Votre programme devra lire, dans l'ordre : l'abscisse minimale, l'abscisse maximale, l'ordonnée minimale et l'ordonnée maximale du rectangle. Il lira ensuite le nombre total de maisons, puis pour chaque maison, son abscisse et son ordonnée.

Votre programme devra déterminer puis afficher le nombre de maisons qui se trouvent dans la zone de recherche. Si une maison est exactement sur le bord de la zone, elle doit ête comptée. 

### Exemple

entrée :

    1
    4
    1
    8
    12
    1
    7
    1
    9
    2
    3
    3
    2
    3
    4
    3
    6
    3
    9
    5
    3
    5
    8
    7
    5
    8
    2
    8
    8

sortie :

    5

### Solution officielle

```python
xMin = int(input())
xMax = int(input())
yMin = int(input())
yMax = int(input())
nbMaisons = int(input())
nbAFouiller = 0
for loop in range(nbMaisons):
   x = int(input())
   y = int(input())
   if (xMin <= x) and (x <= xMax) and (yMin <= y) and (y <= yMax):
      nbAFouiller = nbAFouiller + 1
print(nbAFouiller)
```


### Solution alternative

```python
x_min = int(input())
x_max = int(input())
y_min = int(input())
y_max = int(input())
nb_maisons = int(input())
coord_maisons = iter((int(input()), int(input())) for _ in range(nb_maisons))
nb_maisons_suspectes = sum(1 for (x, y) in coord_maisons if (x_min <= x <= x_max) and (y_min <= y <=y_max))
print(nb_maisons_suspectes)
```

Et une variante avec un style encore plus fonctionnel, mais non recommandée.

```python
est_suspecte = lambda coord: (x_min <= coord[0] <= x_max) and (y_min <= coord[1] <=y_max)
nb_maisons_suspectes = sum(1 for _ in filter(est_suspecte, coord_maisons))
```

## Nombre de jours dans le mois

Écrivez un programme qui lit un numéro de mois algoréen, et affiche le nombre de jours de celui-ci. Les Algoréens disposent de leur propre calendrier. Voici les informations dont vous avez besoin : 


|Numéro du mois | Nombre de jours|
|:---:|:---:|
|1|30|
|2|30|
|3|30|
|4|31|
|5|31|
|6|31|
|7|30|
|8|30|
|9|30|
|1|31|
|1|29|

### Exemple

entrée :

    6

sortie :

    31

### Solution officielle

```python
numero = int(input())
if numero == 11:
   print(29)
else:
   if ( (4 <= numero) and (numero <= 6) ) or (numero == 10):
      print(31)
   else:
      print(30)
```

### Solution alternative

On peut utiliser, au lieu de conditions, une table de valeurs.

```python
nb_jours = [-1, 30, 30, 30, 31, 31, 31, 30, 30, 30, 31, 29]

numéro = int(input())
print(nb_jours[numéro])
```

Remarque
: le $-1$ de la liste, correspond au mois d'indice $0$ qui n'existe pas. On peut mettre ce qu'on veut à la place de $-1$, comme $0$ ou `None`. Cependant, pour avoir un un tableau homogène en type de donnée, on pourrait recommander de ne pas mettre `None`.

## Amitié entre gardes

### Sujet

 Vous devez écrire un programme qui détermine si deux soldats ont été de garde en même temps.

Votre programme doit lire quatre entiers : la date du début et la date de fin (incluse) du service du premier soldat puis celles du second soldat.

Si les deux soldats ont, à un moment (même une seule seconde), été de garde en même temps le programme devra écrire "Amis" et sinon "Pas amis".

### Exemples
#### Exemple 1

entrée :

    2
    5
    3
    6

sortie :

    Amis

#### Exemple 2

entrée :

    1
    5
    10
    15

sortie :

    Pas amis

#### Exemple 3

entrée :

    2
    4
    4
    6

sortie :

    Amis

### Solution officielle

```python
dateDebutPremier = int(input())
dateFinPremier = int(input())
dateDebutSecond = int(input())
dateFinSecond = int(input())
if (dateFinSecond < dateDebutPremier) or (dateFinPremier < dateDebutSecond):
   print("Pas amis")
else:
   print("Amis")
```

Remarque
: Il est simple de justifier qu'on est `Pas amis` : soit le premier est parti quand le second arrive, soit l'inverse !
: Sinon, `Amis` correspond à l'autre cas.
### Solution alternative

* En utilisant la loi de De Morgan, on peut donner une condition aussi rapide qui valide "Amis" au lieu de "Pas amis".

$$\text{non}(A \text{ ou } B) = \text{non}(A)\text{ et }\text{non}(B)$$

* On place cette condition dans une fonction. Elle pourra être utile.
* On utilise l'opérateur ternaire, pour factoriser le `print`.

```python
def intersecte(début_1: int, fin_1: int, début_2: int, fin_2: int) -> bool:
    """Renvoie un booléen.
    Les deux intervalles s'intersectent-ils ?
    Remarque, ici les bords ne comptent pas !
    >>> intersecte(2, 10, 5, 17)
    True
    >>> intersecte(2, 5, 10, 17)
    False
    >>> intersecte(2, 8, 8, 17)
    True
    """
    return (fin_2 >= début_1) and (fin_1 >= début_2)

début_1 = int(input())
fin_1 = int(input())
début_2 = int(input())
fin_2 = int(input())

print("Amis" if intersecte(début_1, fin_1, début_2, fin_2) else "Pas amis")
```

## Casernes de pompiers

### Sujet

 Votre programme doit lire la description de plusieurs paires de zones rectangulaires, et pour chacune, déterminer si les deux rectangles s'intersectent.

Vous devez lire un premier entier, le nombre de paires de zones que votre programme devra tester. Ensuite, pour chaque paire possible, deux zones rectangulaires et parallèles aux axes vous sont données l'une après l'autre. Chaque zone est décrite par 4 entiers : son abscisse minimale et maximale puis son ordonnée minimale et maximale. 

Pour chaque paire de zones, votre programme doit écrire "OUI" si les zones s'intersectent et "NON" sinon. Si elles ne font que se toucher sur les bords il doit écrire "NON".

### Exemple

entrée :

    1
    1
    6
    1
    5
    4
    9
    3
    8

sortie :

    OUI

### Solution officielle

```python
nbPaires = int(input())
for loop in range(nbPaires):
   xMin1 = int(input())
   xMax1 = int(input())
   yMin1 = int(input())
   yMax1 = int(input())
   xMin2 = int(input())
   xMax2 = int(input())
   yMin2 = int(input())
   yMax2 = int(input())
   if ( (xMax2 <= xMin1) or (xMax1 <= xMin2) ) or ( (yMax2 <= yMin1) or (yMax1 <= yMin2) ):
      print("NON")
   else:
      print("OUI")
```

### Solution alternative

```python
def intersecte(début_1: int, fin_1: int, début_2: int, fin_2: int) -> bool:
    """Renvoie un booléen.
    Les deux intervalles s'intersectent-ils ?
    Remarque, ici les bords ne comptent pas !
    >>> intersecte(2, 10, 5, 17)
    True
    >>> intersecte(2, 5, 10, 17)
    False
    >>> intersecte(2, 8, 8, 17)
    False
    """
    return (fin_2 > début_1) and (fin_1 > début_2)

nb_paires = int(input())
for _ in range(nb_paires):
   x_min1 = int(input())
   x_max1 = int(input())
   y_min1 = int(input())
   y_max1 = int(input())
   x_min2 = int(input())
   x_max2 = int(input())
   y_min2 = int(input())
   y_max2 = int(input())
   if intersecte(x_min1, x_max1, x_min2, x_max2) and intersecte(y_min1, y_max1, y_min2, y_max2):
      print("OUI")
   else:
      print("NON")
```

Remarque
: On a ici modifié la fonction `intersecte` pour ne pas prendre en compte les bords comme dans l'exercice précédent !

## Personne disparue

### Sujet

 On vous donne un entier, le numéro d'une personne recherchée, puis un entier tailleListe, et enfin tailleListe entiers parmi lesquels vous devez chercher le numéro de la personne. Si le numéro est présent dans la liste (il peut l'être plusieurs fois) vous devez afficher le texte "Sorti de la ville" sinon "Encore dans la ville".

### Exemple

entrée :

    42
    5
    1
    7
    172
    2
    41

sortie :

    Encore dans la ville

### Solution officielle

```python
numeroPersonne = int(input())
tailleListe = int(input())
estSorti  = False
for loop in range(tailleListe):
   numero = int(input())
   if numero == numeroPersonne:
      estSorti = True
if estSorti:
   print("Sorti de la ville")
else:
   print("Encore dans la ville")
```

### Solution alternative (hors programme ici)

Avec un style fonctionnel.

```python
num_cherché = int(input())
nb_numéros = int(input())
numéros = iter(int(input()) for _ in range(nb_numéros))

est_sorti = any(num_cherché == num for num in numéros)
print("Sorti de la ville" if est_sorti else "Encore dans la ville")
```

* `iter` construit un itérateur prêt à renvoyer les numéros lus sur l'entrée standard. Prêt, mais qui ne construit pas pour autant la liste ; il égrène un à un ces éléments à la demande.
* `any` va demander les éléments de `numéros`, un à un, jusqu'à ce qu'un (*any*) satisfasse la condition `num_cherché == num` ; à ce moment il renvoie `True`. Si l'itérateur est épuisé sans succès, `any`renvoie `False`.
* `est_sorti` est donc un booléen dont on sert avec l'opérateur ternaire `<valeur_si_vrai> if <condition> else <valeur_si_faux>`.


> **Exercice** : Résoudre [La grande fête](http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=1981) avec un style fonctionnel.

## L'espion est démasqué !

### Sujet

 Votre programme doit lire entier : un nombre de personnes à considérer. Ensuite, pour chaque personne, il doit lire son signalement sous la forme de cinq entiers : sa taille en centimètres, son âge en années, son poids en kilogrammes, un entier valant 1 si la personne possède un cheval et 0 sinon, et un entier valant 1 si la personne à les cheveux bruns et 0 sinon.

On veut déterminer pour chaque personne à quel point elle correspond aux 5 critères suivants :

* il aurait une taille supérieure ou égale à 178 cm et inférieure ou égale à 182 cm ;
* il aurait au moins 34 ans ;
* il pèserait strictement moins de 70 kg ;
* il n'a pas de cheval ;
* il a les cheveux bruns.

Lorsque cela n'est pas précisé explicitement, les inégalités sont au sens large.

Pour chaque personne, vous devez tester tous les critères. S'ils sont vérifiés tous les 5, vous devez afficher « Très probable ». Si seulement 3 ou 4 sont vérifiés, vous devez afficher « Probable ». Si aucun n'est vérifié, vous devez afficher « Impossible », et dans les autres cas, vous devez afficher « Peu probable ».
Exemple

entrée :

    1
    180
    40
    65
    0
    1

sortie :

    Très probable

### Solution officielle

```python
nbPersonnes = int(input())
for loop in range(nbPersonnes):
   nbCriteres = 0
   taille = int(input())
   if (178 <= taille) and (taille <= 182):
      nbCriteres = nbCriteres + 1
   age = int(input())
   if age >= 34:
      nbCriteres = nbCriteres + 1
   poids = int(input())
   if poids < 70:
      nbCriteres = nbCriteres + 1
   aCheval = int(input())
   if aCheval == 0:
      nbCriteres = nbCriteres + 1
   aLesCheveuxBruns = int(input())
   if aLesCheveuxBruns == 1:
      nbCriteres = nbCriteres + 1
   
   if nbCriteres == 0:
      print("Impossible")
   elif nbCriteres == 5:
      print("Très probable")
   elif nbCriteres >= 3:
      print("Probable")
   else:
      print("Peu probable")
```

### Solution alternative

* On utilise une table de résultats (`conclusion`) ; utile pour une fonction ayant peu d'antécédents.
* On utilise le transtypage explicite booléen vers entier. `int(True) == 1` et `int(False) == 0`

```python
conclusion = ["Impossible", "Peu probable", "Peu probable", "Probable", "Probable", "Très probable"]

nb_personnes = int(input())
for _ in range(nb_personnes):
    taille = int(input())
    âge = int(input())
    poids = int(input())
    avec_cheval = int(input())
    est_brun = int(input())
    
    nb_critères =  int(178 <= taille <= 182)
    nb_critères += int(âge >= 34)
    nb_critères += int(poids < 70)
    nb_critères += int(avec_cheval == 0)
    nb_critères += int(est_brun == 1)
    
    print(conclusion[nb_critères])
```
---

---
## Au sujet du transtypage
Ceci est un **Complément de cours**, hors programme.


Pour le *fun*, même si c'est mal, on peut écrire une solution en une seule ligne à ce dernier problème.

```python
for _ in range(int(input())): print(["Impossible", "Peu probable", "Peu probable", "Probable", "Probable", "Très probable"][(178<=int(input())<=182) + (int(input())>=34) + (int(input())<70) + (0==int(input())) + (1==int(input()))])
```

:warning: Dans cette variante, le transtypage booléen vers entier est implicite. Cette notion n'est pas au programme ! Par exemple, avec explication :
* `True + True == 2`, on ne sait pas additionner des booléens, donc Python les transtype automatiquement en entier, et calcule `1 + 1 == 2`.
* `True + True * False == 1`, l'opération prioritaire conduit au transtypage `True * False == 1 * 0 == 0`, puis *Python* considère `True + 0`, seul le premier est à transtyper, on a `1 + 0 == 1`.

:warning: Le transtypage fonctionne aussi dans l'autre sens. Par exemple :
* `if 42: print("OK")` affiche `OK`, en effet, après un `if` on attend un booléen, si ce n'en ai pas un *Python* fait une conversion de type automatique (transtypage). Avec les règles :
* L'entier zéro donne `False` ;
* Tout autre entier donne `True` ;
* Une liste (ou ensemble, ...) vide donne `False` ;
* Toute liste (ou ensemble, ...) non vide donne `True` ;
* `None` donne `False`.

Ces pratiques sont parfois considérées comme mauvaises ; les changements de type devant être explicites.

**À retenir**
: Si vous voulez faire du transtypage, faite-le **explicitement** ; comme depuis toujours avec les exemples que vous connaissez déjà :

```python
x = float(input())
n = int(input())
mots = list(input().split())
n_en_texte = str(n)
# etc
```
