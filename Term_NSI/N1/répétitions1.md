# [Répétitions d'instructions](http://www.france-ioi.org/algo/chapter.php?idChapter=643)

> Correction alternative de certains problèmes

## Punition

### Sujet
Votre programme doit écrire 135 fois la phrase : "Je dois respecter le Grand Sorcier.", en plaçant cette phrase exactement une fois sur chaque ligne. Attention, si votre programme n'affiche pas exactement cette phrase avec les points et la majuscule là où il faut, il faudra tout recommencer.

Important : votre programme ne doit pas faire plus d'une douzaine de lignes.

### Solution officielle

```python
for loop in range(135):
   print("Je dois respecter le Grand Sorcier.")
```

### Solution alternative

```python
print("Je dois respecter le Grand Sorcier.\n" * 135, end="")
```

La concaténation des chaînes de caractères permet d'avoir : `"Bon" + "jour" == "Bonjour"`.

De même `"bon" + "bon == "bonbon" == "bon" * 2`.

Nous avons créé notre sortie avec la phrase à écrire, terminée par un saut de ligne `\n`, et concaténée 135 fois avec elle-même.

On termine le `print` avec `end=""` pour ne pas avoir deux sauts de lignes en fin d'affichage, même s'il est accepté.

## Page d'écriture

### Sujet
Votre programme doit écrire 3 lignes, chacune contenant plusieurs fois de suite une lettre suivie du caractère « _ » (underscore en anglais) : la lettre « a » sur la première ligne, la lettre « b » sur la deuxième et la lettre « c » sur la troisième.

Vous disposez déjà d'un modèle où chaque ligne contient 4 lettres :

    a_a_a_a_ 
    b_b_b_b_
    c_c_c_c_

Cependant, vous vous dites qu'il serait mieux de mettre 30 lettres par ligne. Écrivez un programme qui étend votre modèle. Bien sûr, vous utiliserez une boucle pour ne pas vous fatiguer à écrire vous-même 30 fois chaque lettre.

### Solution officielle

```python
for loop in range(30):
   print("a_", end = "")
print()
for loop in range(30):
   print("b_", end = "")
print()
for loop in range(30):
   print("c_", end = "")
print()
```

### Solution alternative

On peut factoriser ce code, en faisant une boucle sur les caractères de `"abc"`.

```python
for lettre in "abc":
    for loop in range(30):
        print(lettre, end = "_")
    print()
```

Remarque, on peut écrire aussi `print(lettre + "_", end = "")`.


## Jeu de dames

### Sujet
Un damier de dimension 4×4 peut se représenter sous la forme suivante :

    OXOX
    XOXO
    OXOX
    XOXO

Votre programme doit afficher un damier de taille $40×40$. Assurez-vous bien que la case tout en haut à gauche contienne un « O », comme c'est le cas dans le damier ci-dessus.

### Solution officielle

```python
for loop in range(20):
   for loop in range(20):
      print("OX", end = "")
   print()
   for loop in range(20):
      print("XO", end = "")
   print()
```

### Solution alternative

1. En Python, on préfère utiliser la variable `_` dans les boucles où on ne se sert pas de la variable de boucle.
2. On peut utiliser la multiplication sur les chaînes de caractères.

```python
for _ in range(20):
    print("OX"*20)
    print("XO"*20)
```

On peut aussi écrire :

```python
for _ in range(20):
    print("OX"*20 + "\n" + "XO"*20)
```

Enfin, on peut aussi écrire une solution sans boucle.

```python
print(("OX"*20 + "\n" + "XO"*20 + "\n") * 20, end="")
```

## Mont Kailash

Votre robot doit faire 108 fois le tour du chemin vert représenté ci-dessous, en tournant dans le sens des aiguilles d'une montre. 

Le robot se trouve initialement en bas à gauche. Chaque case représente 1 km, donc pour faire un tour, le robot doit se déplacer successivement de 13 km dans chacune des 4 directions. 

### Solution officielle

```python
from robot import *
for loop in range(108):
   for loop in range(13):
      haut()
   for loop in range(13):
      droite()
   for loop in range(13):
      bas()
   for loop in range(13):
      gauche()
```

### Solution alternative

On peut factoriser le code.

```python
from robot import *
for _ in range(108):
    for action in [haut, droite, bas, gauche]:
        for _ in range(13):
            action()
```

1. `[haut, droite, bas, gauche]` représente une liste de fonctions.
2. `action` sera donc l'une de ces fonctions, tour à tour.
3. `action()` provoque l'exécution de la fonction, ici sans paramètre.
4. Ce n'est pas gênant d'avoir une double boucle qui utilise la même variable inutilisée `loop` ou bien `_`.
