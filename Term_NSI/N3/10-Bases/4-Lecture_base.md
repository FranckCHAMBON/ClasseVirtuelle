# [Lecture dans une base quelconque](http://www.france-ioi.org/algo/task.php?idChapter=565&idTask=1747)



Vous désirez créer un programme qui permet d'écrire sous le format classique (en base 10) un entier fourni dans une base quelconque. Votre programme doit lire un entier baseDépart, la base de départ, puis un entier nbChiffres, le nombre de chiffres de l'entier à lire en base baseDépart. Votre programme doit ensuite lire sur la ligne suivante nbChiffres entiers correspondant à l'écriture en base baseDépart de l'entier à convertir. Il doit alors afficher cet entier sous le format classique.

## Contraintes

* `1 <= nbChiffres <= 26`
* `2 <= baseDépart <= 100` 

On garantit que l'entier à convertir est plus petit que 100 000 000.

### Exemple

entrée :

    12 2
    3 11

sortie :

    47

## Solution

```python
def lire_base(base: int, chiffres: list) -> int:
    """Renvoie la valeur du nombre, avec ses 'chiffres' donnés en 'base'.
    >>> lire_base(12, [3, 11])
    47
    """
    résultat = 0
    for chiffre in chiffres:
        résultat *= base
        résultat += chiffre
    return résultat

base, nb_chiffres = map(int, input().split())
chiffres = map(int, input().split())

print(lire_base(base, chiffres))
```

### Commentaires

* Pour la lecture, on ne sert pas de `nb_chiffres`, on peut faire facilement la boucle en Python sur `chiffres` sans avoir besoin de `nb_chiffres`.
* La lecture de `chiffres` ne donne pas ici une véritable liste, mais un objet `map` sur lequel on peut itérer comme si c'était une liste. L'avantage étant que la liste n'est pas construite entièrement en mémoire, mais seulement construite à la volée et égrainée à la demande.
* On peut proposer une version récursive de la fonction `lire_base` ; uniquement à but pédagogique :

```python
def lire_base(base: int, chiffres: list) -> int:
    if chiffres == []:
        return 0
    else:
        return chiffres[-1] + base * lire_base(base, chiffres[:-1])

base, nb_chiffres = map(int, input().split())
chiffres = list(map(int, input().split()))

print(lire_base(base, chiffres))
```
* Dans ce cas, la lecture des chiffres doit aboutir à une vraie liste, de manière à utiliser les indices.
* `chiffres[-1]` correspond au dernier chiffre.
* `chiffres[:-1]` correspond à la liste de tous les chiffres... sauf le dernier. Du début à la fin, en excluant la fin.
